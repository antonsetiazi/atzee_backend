# accounting/entities/cash_flow.py

from decimal import Decimal

from core.entities.contracts import BaseEntity

from accounting.models import AccountLedger
from accounting.enum.permissions import AccountingPermission


class CashFlowEntity(BaseEntity):
    key = "accounting.reports.cash_flow"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_REPORT_VIEW

    def query(self, *, user, tenant, query: dict):

        ledgers = AccountLedger.objects.filter(
            tenant=tenant
        ).select_related("account")

        operating = []
        investing = []
        financing = []

        total_operating = Decimal("0")
        total_investing = Decimal("0")
        total_financing = Decimal("0")

        for ledger in ledgers:

            account = ledger.account

            amount = Decimal(ledger.debit) - Decimal(ledger.credit)

            item = {
                "account_code": account.code,
                "account_name": account.name,
                "amount": float(amount),
            }

            # =========================================
            # OPERATING
            # =========================================
            if account.account_type in [
                "revenue",
                "expense",
            ]:
                operating.append(item)
                total_operating += amount

            # =========================================
            # INVESTING
            # =========================================
            elif (
                account.account_type == "asset"
                and account.code.startswith("15")
            ):
                investing.append(item)
                total_investing += amount

            # =========================================
            # FINANCING
            # =========================================
            elif account.account_type in [
                "liability",
                "equity",
            ]:
                financing.append(item)
                total_financing += amount

        net_cash_flow = (
            total_operating
            + total_investing
            + total_financing
        )

        return {
            "operating": operating,
            "investing": investing,
            "financing": financing,

            "total_operating": float(total_operating),
            "total_investing": float(total_investing),
            "total_financing": float(total_financing),

            "net_cash_flow": float(net_cash_flow),
        }