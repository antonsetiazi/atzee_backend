# accounting/entities/profit_loss.py

from decimal import Decimal
from django.db.models import Sum

from core.entities.contracts import BaseEntity

from accounting.models import Account, AccountLedger
from accounting.enum.permissions import AccountingPermission


class ProfitLossEntity(BaseEntity):
    key = "accounting.profit.loss"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_ACCOUNT_VIEW

    def query(self, *, user, tenant, query: dict):

        accounts = Account.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
            is_group=False,
            account_type__in=["revenue", "expense"],
        ).order_by("code")

        revenues = []
        expenses = []

        total_revenue = Decimal("0")
        total_expense = Decimal("0")

        for acc in accounts:

            agg = AccountLedger.objects.filter(
                tenant=tenant,
                account=acc,
            ).aggregate(
                debit=Sum("debit"),
                credit=Sum("credit"),
            )

            debit = agg["debit"] or Decimal("0")
            credit = agg["credit"] or Decimal("0")

            # 🔥 NORMAL ACCOUNTING LOGIC
            if acc.account_type == "revenue":
                balance = credit - debit

                revenues.append({
                    "account_code": acc.code,
                    "account_name": acc.name,
                    "amount": balance,
                })

                total_revenue += balance

            elif acc.account_type == "expense":
                balance = debit - credit

                expenses.append({
                    "account_code": acc.code,
                    "account_name": acc.name,
                    "amount": balance,
                })

                total_expense += balance

        net_profit = total_revenue - total_expense

        return {
            "revenues": revenues,
            "expenses": expenses,

            "total_revenue": total_revenue,
            "total_expense": total_expense,

            "net_profit": net_profit,
        }