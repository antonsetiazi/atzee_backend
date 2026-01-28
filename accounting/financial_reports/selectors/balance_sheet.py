from django.db.models import Sum
from accounting.ledger.models import LedgerEntry
from core.tenants.models import Tenant


def get_balance_sheet(
    *,
    tenant: Tenant,
    as_of_date,
):
    qs = (
        LedgerEntry.objects
        .filter(
            tenant=tenant,
            entry_date__lte=as_of_date,
            account__category__in=[
                "ASSET",
                "LIABILITY",
                "EQUITY",
            ],
            journal__status="POSTED"
        )
        .values(
            "account__code",
            "account__name",
            "account__category",
            "account__normal_balance",
        )
        .annotate(
            total_debit=Sum("debit"),
            total_credit=Sum("credit"),
        )
        .order_by("account__code")
    )

    assets = []
    liabilities = []
    equity = []

    total_assets = 0
    total_liabilities = 0
    total_equity = 0

    for row in qs:
        debit = row["total_debit"] or 0
        credit = row["total_credit"] or 0

        balance = (
            debit - credit
            if row["account__normal_balance"] == "DEBIT"
            else credit - debit
        )

        data = {
            "account_code": row["account__code"],
            "account_name": row["account__name"],
            "balance": balance,
        }

        if row["account__category"] == "ASSET":
            assets.append(data)
            total_assets += balance
        elif row["account__category"] == "LIABILITY":
            liabilities.append(data)
            total_liabilities += balance
        else:
            equity.append(data)
            total_equity += balance

    return {
        "assets": assets,
        "liabilities": liabilities,
        "equity": equity,
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "total_equity": total_equity,
        "balanced": total_assets == (total_liabilities + total_equity),
    }
    