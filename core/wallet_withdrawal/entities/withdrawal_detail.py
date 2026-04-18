# core/wallet_withdrawal/entities/withdrawal_detail.py

from core.entities.contracts import BaseEntity
from core.wallet_withdrawal.models.withdrawal import Withdrawal

from core.enum.permissions import CorePermission


class WithdrawalDetailEntity(BaseEntity):
    key = "withdrawals.detail"
    domain = "core"
    permission = CorePermission.ADMIN_WALLET_WITHDRAWAL_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:
        withdrawal_id = query.get("id")

        withdrawal = (
            Withdrawal.objects
            .filter(
                tenant=tenant,
                id=withdrawal_id,
            )
            .select_related("user", "wallet")
            .first()
        )

        if not withdrawal:
            raise Exception("Withdrawal not found")

        destination = withdrawal.destination or {}

        amount = float(withdrawal.amount)
        fee = float(withdrawal.fee)

        bank_name = destination.get("bank_name", "-")
        account_number = destination.get("account_number", "-")
        account_name = destination.get("account_name", "-")

        return {
            "id": str(withdrawal.id),

            # 👤 user
            "user_name": withdrawal.user.full_name or withdrawal.user.username,
            "user_phone": withdrawal.user.phone or "-",

            # 💰 finance
            "amount": amount,
            "fee": fee,
            "net_amount": amount - fee,

            # 🏦 destination
            "destination_label": f"{bank_name} • {account_number} • {account_name}",

            # status
            "status": withdrawal.status,

            # default form values
            "decision": "",
            "reason": "",
        }