# core/master/uom/entities/uom_list.py

from core.entities.contracts import BaseEntity
from core.master.uom.models import UOM


class UOMListEntity(BaseEntity):
    """
    uom.list entity
    """

    key = "uom.list"
    domain = "core"
    permission = "core.uom.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = UOM.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).select_related("category")

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(u.id),
                "code": u.code,
                "name": u.name,
                "category": u.category.name,
                "precision": u.precision,
                "is_base": u.is_base,
            }
            for u in items
        ]

        return {
            "items": data,
            "total": total,
        }
