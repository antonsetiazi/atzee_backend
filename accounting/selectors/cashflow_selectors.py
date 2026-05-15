# accounting/selectors/cashflow_selectors.py

from collections import defaultdict
from decimal import Decimal

from accounting.models import AccountLedger

MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


def get_monthly_cash_flow(
    *,
    tenant,
):
    cash_flow_map = defaultdict(Decimal)

    cash_ledgers = (
        AccountLedger.objects.filter(
            tenant=tenant,
            account__code__startswith="11",
        )
        .select_related("account")
        .order_by("created_at")
    )

    for ledger in cash_ledgers:
        month = ledger.created_at.strftime("%b")
        amount = Decimal(ledger.debit) - Decimal(ledger.credit)
        cash_flow_map[month] += amount

    results = []

    for month in MONTHS:
        results.append(
            {
                "month": month,
                "value": float(cash_flow_map.get(month, 0)),
            }
        )

    return results
