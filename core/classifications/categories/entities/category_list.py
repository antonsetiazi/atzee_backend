# core/classifications/categories/entities/category_list.py

from core.entities.contracts import BaseEntity
from core.classifications.categories.models import Category


class CategoryListEntity(BaseEntity):
    """
    categories.list entity
    """

    key = "categories.list"
    domain = "core"
    permission = "core.categories.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Category.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).select_related("parent")

        # optional filters
        scope = query.get("scope")
        if scope:
            qs = qs.filter(scope=scope)

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        qs = qs.order_by("scope", "name")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(c.id),
                "scope": c.scope,
                "code": c.code,
                "name": c.name,
                "parent": c.parent.name if c.parent else None,
            }
            for c in items
        ]

        return {
            "items": data,
            "total": total,
        }
