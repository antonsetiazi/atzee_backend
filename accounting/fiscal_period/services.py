from decimal import Decimal
from django.db import transaction
from django.utils import timezone

from accounting.fiscal_period.models import FiscalPeriod
from accounting.ledger.models import LedgerEntry
from accounting.journals.services import (
    create_journal,
    add_journal_line,
    post_journal
)
from accounting.chart_of_accounts.selectors import get_account_by_code
from accounting.journals.constants import JournalType


@transaction.atomic
def close_fiscal_period(
    *,
    tenant,
    period: FiscalPeriod,
    closed_by,
):
    """
    Close fiscal period and move net profit to retained earnings.
    """

    if period.is_closed:
        raise ValueError("Fiscal period already closed.")
    
    # 1. Calculate net profit
    qs = LedgerEntry.objects.filter(
        tenant=tenant,
        entry_date__range=(period.start_date, period.end_date),
        account__category__in=["INCOME", "EXPENSE"],
        journal__status="POSTED"
    )

    total_income = Decimal("0")
    total_expense = Decimal("0")

    for row in qs:
        if row.account.category == "INCOME":
            total_income += row.credit - row.debit
        else:
            total_expense += row.debit - row.credit

    net_profit = total_income - total_expense

    # 2. Create closing journal
    retained_earnings = get_account_by_code(
        tenant=tenant,
        code="3200"
    )

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

    if net_profit > 0:
        # Credit retained earnings
        add_journal_line(
            journal=journal,
            account=retained_earnings,
            debit=Decimal("0"),
            credit=net_profit,
            memo="Net profit transfer"
        )

    elif net_profit < 0:
        # Debit retained earnings
        add_journal_line(
            journal=journal,
            account=retained_earnings,
            debit=abs(net_profit),
            credit=Decimal("0"),
            memo="Net loss transfer"
        )

    post_journal(
        journal=journal,
        posted_by=closed_by
    )

    # 3.  Lock period
    period.is_closed = True
    period.closed_at = timezone.now()
    period.closed_by = closed_by
    period.save(update_fields=[
        "is_closed",
        "closed_at",
        "closed_by"
    ])