# core/legal/entities/policy_detail.py

from core.entities.contracts import BaseEntity
from core.legal.models import PolicyDocument

from core.enum.permissions import CorePermission


class PolicyDetailEntity(BaseEntity):
    key = "legal.policies.detail"
    domain = "core"
    permission = CorePermission.ADMIN_POLICY_EDIT

    def query(self, *, user, tenant, query: dict):

        policy = PolicyDocument.objects.filter(
            tenant=tenant,
            id=query.get("id"),
            is_deleted=False,
        ).first()

        if not policy:
            raise Exception("Policy not found")

        return {
            "id": str(policy.id),
            "code": policy.code,
            "title": policy.title,
            "content": policy.content,
            "is_active": policy.is_active,
        }