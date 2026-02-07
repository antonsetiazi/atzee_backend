# accounting/fiscal_period/closing.py

from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from django.db.models import Sum
from accounting.fiscal_period.models import FiscalPeriod
from accounting.journals.services import create_journal, add_journal_line, post_journal
from accounting.chart_of_accounts.selectors import get_account_by_code
from accounting.journals.constants import JournalType, JournalStatus
from accounting.chart_of_accounts.models import AccountType

@transaction.atomic
def close_fiscal_period_logic(*, tenant, period: FiscalPeriod, closed_by):
    """
    Close fiscal period by:
    - Closing income & expense accounts
    - Transfer net profit/loss to retained earnings
    """
    if period.is_closed:
        raise ValueError("Fiscal period already closed.")

    # 1. Aggregate balances
    balances = (
        period.ledgerentry_set.filter(
            tenant=tenant,
            entry_date__range=(period.start_date, period.end_date),
            journal__status=JournalStatus.POSTED,
            account__account_type__in=[AccountType.INCOME, AccountType.EXPENSE],
        )
        .values("account_id", "account__account_type")
        .annotate(total_debit=Sum("debit"), total_credit=Sum("credit"))
    )

    if not balances:
        raise ValueError("No ledger activity in fiscal period.")

    # 2. Create closing journal
    journal = create_journal(
        tenant=tenant,
        created_by=closed_by,
        journal_number=f"CLOSE-{period.name}",
        journal_type=JournalType.CLOSING,
        journal_date=period.end_date,
        description=f"Closing fiscal period {period.name}",
        source_app="fiscal_period",
        source_id=str(period.id),
    )

    net_profit = Decimal("0")

    # 3. Close each income & expense account
    for row in balances:
        debit = row["total_debit"] or Decimal("0")
        credit = row["total_credit"] or Decimal("0")
        balance = credit - debit
        if balance == 0:
            continue

        account_id = row["account_id"]
        account_type = row["account__account_type"]

        if account_type == AccountType.INCOME:
            add_journal_line(journal=journal, account_id=account_id, debit=balance, credit=Decimal("0"), memo="Closing income account")
            net_profit += balance
        elif account_type == AccountType.EXPENSE:
            add_journal_line(journal=journal, account_id=account_id, debit=Decimal("0"), credit=abs(balance), memo="Closing expense account")
            net_profit -= abs(balance)

    # 4. Retained earnings
    retained_earnings = get_account_by_code(tenant=tenant, code="3200")
    if net_profit > 0:
        add_journal_line(journal=journal, account=retained_earnings, debit=Decimal("0"), credit=net_profit, memo="Net profit transfer")
    elif net_profit < 0:
        add_journal_line(journal=journal, account=retained_earnings, debit=abs(net_profit), credit=Decimal("0"), memo="Net loss transfer")

    # 5. Post journal
    post_journal(journal=journal, posted_by=closed_by)

    # 6. Lock period
    period.is_closed = True
    period.closed_at = timezone.now()
    period.closed_by = closed_by
    period.save(update_fields=["is_closed", "closed_at", "closed_by"])
