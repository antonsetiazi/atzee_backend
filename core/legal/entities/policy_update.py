# core/legal/entities/policy_update.py

from core.entities.contracts import BaseEntity
from core.legal import services
from core.legal import selectors

from core.enum.permissions import CorePermission


class PolicyUpdateEntity(BaseEntity):
    key = "legal.policies.update"
    domain = "core"
    permission = CorePermission.ADMIN_POLICY_EDIT

    def query(self, *, user, tenant, query: dict):
        return {}

    def execute(self, *, user, tenant, data: dict):

        old_policy = selectors.get_policy_by_id(
            tenant=tenant,
            policy_id=data["id"],
        )

        if not old_policy:
            raise Exception("Policy not found")
        
        # 🔥 CREATE NEW VERSION
        new_policy = services.create_policy(
            tenant=tenant,
            created_by=user,
            code=old_policy.code,
            policy_type=old_policy.policy_type,
            title=data.get("title") or old_policy.title,
            content=data.get("content") or old_policy.content,
        )

        # 🔒 deactivate old version
        old_policy.is_active = False
        old_policy.updated_by = user
        old_policy.save(update_fields=["is_active", "updated_by", "updated_at"])

        return {
            "success": True,
            "message": "Versi baru policy berhasil dibuat",
            "id": str(new_policy.id),
        }