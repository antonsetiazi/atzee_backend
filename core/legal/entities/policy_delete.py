# core/legal/entities/policy_delete.py

from core.entities.contracts import BaseEntity
from core.legal.models import PolicyDocument

from core.enum.permissions import CorePermission


class PolicyDeleteEntity(BaseEntity):
    key = "legal.policies.delete"
    domain = "core"
    permission = CorePermission.ADMIN_POLICY_DELETE

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:
        policy_id = data.get("id")

        policy = PolicyDocument.objects.filter(
            tenant=tenant,
            id=policy_id,
            is_deleted=False,
        ).first()

        if not policy:
            raise Exception("Policy not found")

        # 🔥 SOFT DELETE
        policy.is_deleted = True
        policy.updated_by = user
        policy.save(update_fields=["is_deleted", "updated_by", "updated_at"])

        return {
            "success": True,
            "message": "Policy berhasil dihapus",
            "id": str(policy.id),
        }