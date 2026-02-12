# core/schedule/recurrings/entities/recurring_select_list.py

from core.entities.contracts import BaseEntity
from core.schedule.recurrings import selectors


class RecurringSelectListEntity(BaseEntity):
    """
    schedule.recurrings.select.list entity
    """

    key = "schedule.recurrings.select.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = selectors.get_recurring_queryset(
            tenant=tenant
        ).order_by("frequency")

        items = [
            {
                "value": str(r.id),
                "label": f"{r.event.title} ({r.frequency})",
            }
            for r in qs
        ]

        return {
            "items": items,
            "total": qs.count()
        }
