# core/classifications/tags/entities/tag_list.py

from core.entities.contracts import BaseEntity
from core.classifications.tags.models import Tag


class TagListEntity(BaseEntity):
    """
    tags.list entity
    """

    key = "tags.list"
    domain = "core"
    permission = "core.classifications.tags.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Tag.objects.filter(
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
        items = qs[offset:limit]

        data = [
            {
                "id": str(t.id),
                "code": t.code,
                "name": t.name,
                "description": t.description,
            }
            for t in items
        ]

        return {
            "items": data,
            "total": total,
        }
