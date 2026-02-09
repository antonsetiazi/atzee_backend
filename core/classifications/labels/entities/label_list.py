# core/classifications/labels/entities/label_list.py

from core.entities.contracts import BaseEntity
from core.classifications.labels.models import Label


class LabelListEntity(BaseEntity):
    """
    labels.list entity
    """

    key = "labels.list"
    domain = "core"
    permission = "core.labels.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Label.objects.filter(
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
                "id": str(label.id),
                "code": label.code,
                "name": label.name,
                "scope": label.scope,
                "description": label.description,
            }
            for label in items
        ]

        return {
            "items": data,
            "total": total,
        }
