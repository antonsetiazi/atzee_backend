# accounting/entities/balance_sheet.py

from decimal import Decimal
from django.db.models import Sum

from core.entities.contracts import BaseEntity

from accounting.models import Account, AccountLedger
from accounting.enum.permissions import AccountingPermission


class BalanceSheetEntity(BaseEntity):
    key = "accounting.balance.sheet"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_ACCOUNT_VIEW

    def query(self, *, user, tenant, query: dict):

        accounts = Account.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
            is_group=False,
            account_type__in=[
                "asset",
                "liability",
                "equity",
            ]
        ).order_by("code")

        assets = []
        liabilities = []
        equities = []

        total_asset = Decimal("0")
        total_liability = Decimal("0")
        total_equity = Decimal("0")

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

            # =========================
            # ASSET
            # =========================
            if acc.account_type == "asset":

                balance = debit - credit

                assets.append({
                    "account_code": acc.code,
                    "account_name": acc.name,
                    "amount": balance,
                })

                total_asset += balance

            # =========================
            # LIABILITY
            # =========================
            elif acc.account_type == "liability":

                balance = credit - debit

                liabilities.append({
                    "account_code": acc.code,
                    "account_name": acc.name,
                    "amount": balance,
                })

                total_liability += balance

            # =========================
            # EQUITY
            # =========================
            elif acc.account_type == "equity":

                balance = credit - debit

                equities.append({
                    "account_code": acc.code,
                    "account_name": acc.name,
                    "amount": balance,
                })

                total_equity += balance

        is_balanced = (
            total_asset ==
            (total_liability + total_equity)
        )

        return {
            "assets": assets,
            "liabilities": liabilities,
            "equities": equities,

            "total_asset": total_asset,
            "total_liability": total_liability,
            "total_equity": total_equity,

            "is_balanced": is_balanced,
        }