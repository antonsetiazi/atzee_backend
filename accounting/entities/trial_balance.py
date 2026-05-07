# accounting/entities/trial_balance.py

from decimal import Decimal

from django.db.models import Sum

from core.entities.contracts import BaseEntity

from accounting.models import Account, AccountLedger
from accounting.enum.permissions import AccountingPermission


class TrialBalanceEntity(BaseEntity):
    key = "accounting.trial.balance"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_ACCOUNT_VIEW

    def query(self, *, user, tenant, query: dict):

        accounts = Account.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
            is_group=False,
        ).order_by("code")

        items = []

        total_debit = Decimal("0")
        total_credit = Decimal("0")

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

            items.append({
                "account_id": str(acc.id),
                "account_code": acc.code,
                "account_name": acc.name,
                "debit": debit,
                "credit": credit,
            })

            total_debit += debit
            total_credit += credit

        return {
            "items": items,
            "total_debit": total_debit,
            "total_credit": total_credit,
            "is_balanced": total_debit == total_credit,
        }