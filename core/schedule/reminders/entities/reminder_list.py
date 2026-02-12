# core/schedule/reminders/entities/reminder_list.py

from core.entities.contracts import BaseEntity
from core.schedule.reminders import selectors


class ReminderListEntity(BaseEntity):
    """
    schedule.reminders.list entity
    """

    key = "schedule.reminders.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = selectors.get_reminder_queryset(tenant=tenant)

        search = query.get("search")
        if search:
            qs = qs.filter(event__title__icontains=search)

        qs = qs.order_by("reminder_time")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))
        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(r.id),
                "event_title": r.event.title,
                "reminder_time": r.reminder_time,
                "reminder_type": r.reminder_type,
                "repeat_interval": r.repeat_interval,
            }
            for r in items
        ]

        return {
            "items": data,
            "total": total
        }

