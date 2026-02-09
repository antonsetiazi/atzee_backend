# core/org/branches/entities/branch_list.py

from core.entities.contracts import BaseEntity
from core.org.branches.models import Branch


class BranchListEntity(BaseEntity):
    """
    branches.list entity
    """

    key = "branches.list"
    domain = "core"
    permission = "core.branches.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Branch.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        )

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("name")[offset:limit]

        data = [
            {
                "id": str(b.id),
                "code": b.code,
                "name": b.name,
            }
            for b in items
        ]

        return {
            "items": data,
            "total": total,
        }
