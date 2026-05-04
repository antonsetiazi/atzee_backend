# core/legal/entities/policy_create.py

from core.entities.contracts import BaseEntity
from core.legal import services

from core.enum.permissions import CorePermission


class PolicyCreateEntity(BaseEntity):
    key = "legal.policies.create"
    domain = "core"
    permission = CorePermission.ADMIN_POLICY_CREATE

    def query(self, *, user, tenant, query: dict):
        return {}

    def execute(self, *, user, tenant, data: dict):

        policy = services.create_policy(
            tenant=tenant,
            created_by=user,
            code=data["code"],
            title=data["title"],
            policy_type=data["policy_type"],
            content=data["content"],
        )

        return {
            "success": True,
            "message": "Policy berhasil dibuat",
            "id": str(policy.id),
        }