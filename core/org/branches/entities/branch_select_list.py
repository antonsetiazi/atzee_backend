# core/org/branches/entities/branch_select_list.py

from core.entities.contracts import BaseEntity
from core.org.branches.models import Branch


class BranchSelectListEntity(BaseEntity):
    """
    branches.select.list entity
    """

    key = "branches.select.list"
    domain = "core"
    permission = "core.branches.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Branch.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).order_by("name")

        items = [
            {
                "value": str(b.id),
                "label": b.name,
            }
            for b in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
