# core/schedule/reminders/entities/reminder_select_list.py

from core.entities.contracts import BaseEntity
from core.schedule.reminders import selectors


class ReminderSelectListEntity(BaseEntity):
    """
    schedule.reminders.select.list entity
    """

    key = "schedule.reminders.select.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = selectors.get_reminder_queryset(tenant=tenant).order_by("reminder_time")

        items = [
            {
                "value": str(r.id),
                "label": f"{r.event.title} ({r.reminder_type})",
            }
            for r in qs
        ]

        return {
            "items": items,
            "total": qs.count()
        }

