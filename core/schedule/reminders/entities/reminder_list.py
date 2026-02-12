# core/schedule/reminders/entities/reminder_list.py

from core.entities.contracts import BaseEntity
from core.schedule.reminders.models import Reminder


class ReminderListEntity(BaseEntity):
    """
    reminders.list entity
    """

    key = "schedule.reminders.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Reminder.objects.filter(tenant=tenant, is_deleted=False)

        search = query.get("search")
        if search:
            qs = qs.filter(title__icontains=search)

        qs = qs.order_by("remind_at")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))
        offset = (page - 1) * page_size
        limit = offset + page_size
        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(r.id),
                "title": r.title,
                "remind_at": r.remind_at,
                "related_event_id": str(r.event.id) if r.event else None,
            }
            for r in items
        ]
        return {"items": data, "total": total}
