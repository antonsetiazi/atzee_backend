# core/wallet_withdrawal/entities/withdrawal_approval.py

from core.entities.contracts import BaseEntity
from core.wallet_withdrawal.models.withdrawal import (
    Withdrawal,
    WithdrawalStatus,
)
from core.wallet_withdrawal.services.withdrawal_processor import (
    mark_as_completed,
    mark_as_failed,
)

from core.enum.permissions import CorePermission


class WithdrawalApprovalEntity(BaseEntity):
    key = "withdrawals.approval"
    domain = "core"
    permission = CorePermission.ADMIN_WALLET_WITHDRAWAL_APPROVE

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:
        withdrawal_id = data.get("id")
        decision = str(data.get("decision", "")).strip().lower()
        reason = data.get("reason", "")

        if not withdrawal_id:
            raise Exception("Withdrawal id is required")

        if decision  not in ["approve", "reject"]:
            raise Exception("Invalid action")

        withdrawal = Withdrawal.objects.filter(
            tenant=tenant,
            id=withdrawal_id,
        ).first()

        if not withdrawal:
            raise Exception("Withdrawal not found")

        # hanya pending yg boleh diproses
        if withdrawal.status != WithdrawalStatus.PENDING:
            raise Exception("Withdrawal already processed")

        # ===============================
        # APPROVE
        # ===============================
        if decision == "approve":
            mark_as_completed(
                withdrawal,
                external_id=f"MANUAL-{withdrawal.id}"
            )

            return {
                "success": True,
                "message": "Withdrawal approved",
                "id": str(withdrawal.id),
            }

        # ===============================
        # REJECT
        # ===============================
        mark_as_failed(
            withdrawal,
            reason=reason or "Rejected by admin"
        )

        return {
            "success": True,
            "message": "Withdrawal rejected",
            "id": str(withdrawal.id),
        }