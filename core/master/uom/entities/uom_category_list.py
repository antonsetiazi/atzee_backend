# core/master/uom/entities/uom_category_list.py

from core.entities.contracts import BaseEntity
from core.master.uom.models import UOMCategory


class UOMCategoryListEntity(BaseEntity):
    """
    uom.categories.list
    """

    key = "uom.categories.list"
    domain = "core"
    permission = "core.uom.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = UOMCategory.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).order_by("name")

        items = [
            {
                "value": str(c.id),
                "label": f"{c.code} - {c.name}",
            }
            for c in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
