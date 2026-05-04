# core/legal/entities/policy_list.py

from core.entities.contracts import BaseEntity
from core.legal.models import PolicyDocument

from core.enum.permissions import CorePermission


class PolicyListEntity(BaseEntity):
    key = "legal.policies.list"
    domain = "core"
    permission = CorePermission.ADMIN_POLICY_VIEW

    def query(self, *, user, tenant, query: dict):

        qs = PolicyDocument.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        search = query.get("search")
        if search:
            qs = qs.filter(title__icontains=search)

        items = qs.order_by("-version")

        return {
            "items": [
                {
                    "id": str(p.id),
                    "code": p.code,
                    "title": p.title,
                    "policy_type": p.policy_type,
                    "version": p.version,
                    "is_active": p.is_active,
                    "created_at": p.created_at,
                }
                for p in items
            ],
            "total": qs.count(),
        }