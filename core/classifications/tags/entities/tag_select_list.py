# core/classifications/tags/entities/tag_select_list.py

from core.entities.contracts import BaseEntity
from core.classifications.tags.models import Tag


class TagSelectListEntity(BaseEntity):
    """
    tags.select.list entity
    """

    key = "tags.select.list"
    domain = "core"
    permission = "core.classifications.tags.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Tag.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).order_by("name")

        items = [
            {
                "value": str(t.id),
                "label": t.name,
            }
            for t in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
