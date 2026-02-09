# core/classifications/categories/entities/category_select_list.py

from core.entities.contracts import BaseEntity
from core.classifications.categories.models import Category


class CategorySelectListEntity(BaseEntity):
    """
    categories.select.list entity
    """

    key = "categories.select.list"
    domain = "core"
    permission = "core.categories.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Category.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        )

        scope = query.get("scope")
        if scope:
            qs = qs.filter(scope=scope)

        qs = qs.order_by("name")

        items = [
            {
                "value": str(c.id),
                "label": c.name,
            }
            for c in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
