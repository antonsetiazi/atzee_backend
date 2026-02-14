# core/widgets/entities/widget_select_list.py

from core.entities.contracts import BaseEntity
from core.widgets.models import UIWidget


class WidgetSelectListEntity(BaseEntity):
    """
    widgets.select.list entity
    """

    key = "widgets.select.list"
    domain = "core"
    permission = "core.widgets.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = UIWidget.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        )

        widget_type = query.get("type")
        if widget_type:
            qs = qs.filter(type=widget_type)

        items = [
            {
                "value": str(w.id),
                "label": f"{w.title or w.type} ({w.position})",
            }
            for w in qs.order_by("order", "-created_at")
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
