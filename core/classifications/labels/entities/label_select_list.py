# core/classifications/labels/entities/label_select_list.py

from core.entities.contracts import BaseEntity
from core.classifications.labels.models import Label


class LabelSelectListEntity(BaseEntity):
    """
    labels.select.list entity
    """

    key = "labels.select.list"
    domain = "core"
    permission = "core.labels.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Label.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).order_by("name")

        items = [
            {
                "value": str(label.id),
                "label": label.name,
            }
            for label in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
