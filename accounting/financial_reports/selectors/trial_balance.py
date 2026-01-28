from django.db.models import Sum
from accounting.ledger.models import LedgerEntry
from core.tenants.models import Tenant


def get_trial_balance(
    *,
    tenant: Tenant,
    start_date,
    end_date,
):
    """
    Return trial balance grouped by account.
    """

    qs = (
        LedgerEntry.objects
        .filter(
            tenant=tenant,
            entry_date__range=(start_date, end_date),
            journal__status="POSTED"
        )
        .values(
            "account__id",
            "account__code",
            "account__name",
            "account__normal_balance"
        )
        .annotate(
            total_debit=Sum("debit"),
            total_credit=Sum("credit"),
        )
        .order_by("account__code")
    )
    
    results = []

    for row in qs:
        debit = row["total_debit"] or 0
        credit = row["total_credit"] or 0

        balance = (
            debit - credit
            if row["account__normal_balance"] == "DEBIT"
            else credit - debit
        )

        results.append({
            "account_code": row["account__code"],
            "account_name": row["account__name"],
            "debit": debit,
            "credit": credit,
            "balance": balance,
        })

    return results