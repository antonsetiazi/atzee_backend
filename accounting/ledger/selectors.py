# accounting/ledger/selectors.py

from django.db.models import QuerySet
from accounting.ledger.models import LedgerEntry
from accounting.chart_of_accounts.models import ChartOfAccount


def ledger_entries_qs(*, tenant) -> QuerySet[LedgerEntry]:
    return (
        LedgerEntry.objects
        .filter(tenant=tenant)
        .select_related("account", "journal")
        .order_by("entry_date", "id")
    )


def ledger_entries_by_account(
    *,
    tenant,
    account: ChartOfAccount,
) -> QuerySet[LedgerEntry]:
    return ledger_entries_qs(tenant=tenant).filter(account=account)


def ledger_entries_by_date_range(
    *,
    tenant,
    start_date,
    end_date,
) -> QuerySet[LedgerEntry]:
    return ledger_entries_qs(tenant=tenant).filter(
        entry_date__range=(start_date, end_date)
    )
