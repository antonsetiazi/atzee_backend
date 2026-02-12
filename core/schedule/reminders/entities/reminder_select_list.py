# core/schedule/reminders/entities/reminder_select_list.py

from core.entities.contracts import BaseEntity
from core.schedule.reminders.models import Reminder


class ReminderSelectListEntity(BaseEntity):
    """
    reminders.select.list entity
    """

    key = "schedule.reminders.select.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Reminder.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).order_by("remind_at")

        items = [
            {
                "value": str(r.id),
                "label": r.title,
            }
            for r in qs
        ]

        return {"items": items, "total": qs.count()}
