# accounting/entities/cash_flow.py

from collections import defaultdict
from decimal import Decimal

from accounting.enum.permissions import AccountingPermission
from accounting.models import AccountLedger
from core.entities.contracts import BaseEntity


class CashFlowEntity(BaseEntity):
    key = "accounting.reports.cash_flow"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_REPORT_VIEW

    def query(self, *, user, tenant, query: dict):

        ledgers = AccountLedger.objects.filter(tenant=tenant).select_related(
            "account"
        )

        # =========================
        # ACCUMULATORS
        # =========================
        operating_map = defaultdict(Decimal)
        investing_map = defaultdict(Decimal)
        financing_map = defaultdict(Decimal)

        account_name_map = {}

        total_operating = Decimal("0")
        total_investing = Decimal("0")
        total_financing = Decimal("0")

        for ledger in ledgers:

            account = ledger.account

            raw_amount = Decimal(ledger.debit) - Decimal(ledger.credit)

            # normalize presentation
            if account.account_type == "revenue":
                amount = raw_amount * Decimal("-1")

            elif account.account_type == "expense":
                amount = raw_amount * Decimal("-1")

            else:
                amount = raw_amount

            # cache account name once
            account_name_map[account.code] = account.name

            # OPERATING
            if account.account_type in ["revenue", "expense"]:
                operating_map[account.code] += amount
                total_operating += amount

            # INVESTING
            elif account.account_type == "asset" and account.code.startswith(
                "15"
            ):
                investing_map[account.code] += amount
                total_investing += amount

            # FINANCING
            elif account.account_type in ["liability", "equity"]:
                financing_map[account.code] += amount
                total_financing += amount

        # =========================
        # BUILD RESULT
        # =========================
        operating = [
            {
                "account_code": code,
                "account_name": account_name_map.get(code, ""),
                "amount": float(amount),
            }
            for code, amount in operating_map.items()
        ]

        investing = [
            {
                "account_code": code,
                "account_name": account_name_map.get(code, ""),
                "amount": float(amount),
            }
            for code, amount in investing_map.items()
        ]

        financing = [
            {
                "account_code": code,
                "account_name": account_name_map.get(code, ""),
                "amount": float(amount),
            }
            for code, amount in financing_map.items()
        ]

        net_cash_flow = total_operating + total_investing + total_financing

        return {
            "operating": operating,
            "investing": investing,
            "financing": financing,
            "total_operating": float(total_operating),
            "total_investing": float(total_investing),
            "total_financing": float(total_financing),
            "net_cash_flow": float(net_cash_flow),
        }
