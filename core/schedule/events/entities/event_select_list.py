# core/schedule/events/entities/event_select_list.py

from core.entities.contracts import BaseEntity
from core.schedule.events.models import Event


class EventSelectListEntity(BaseEntity):
    """
    events.select.list entity
    """

    key = "schedule.events.select.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Event.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).order_by("start_datetime")

        items = [
            {
                "value": str(e.id),
                "label": e.title,
            }
            for e in qs
        ]

        return {"items": items, "total": qs.count()}
