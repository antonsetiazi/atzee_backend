from django.db.models import Sum
from accounting.ledger.models import LedgerEntry
from core.tenants.models import Tenant


def get_profit_and_loss(
    *,
    tenant: Tenant,
    start_date,
    end_date,
):
    qs = (
        LedgerEntry.objects
        .filter(
            tenant=tenant,
            entry_date__range=(start_date, end_date),
            account__category__in=["INCOME", "EXPENSE"],
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

    income = []
    expense = []

    total_income = 0
    total_expense = 0

    for row in qs:
        debit = row["total_debit"] or 0
        credit = row["total_credit"] or 0

        amount = (
            credit - debit
            if row["account__normal_balance"] == "CREDIT"
            else debit - credit
        )

        data = {
            "account_code": row["account__code"],
            "account_name": row["account__name"],
            "amount": amount,
        }

        if row["account__category"] == "INCOME":
            income.append(data)
            total_income += amount
        else:
            expense.append(data)
            total_expense += amount

    return {
        "income": income,
        "expense": expense,
        "total_income": total_income,
        "total_expense": total_expense,
        "net_profit": total_income - total_expense,
    }