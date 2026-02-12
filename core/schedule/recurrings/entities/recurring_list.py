# core/schedule/recurrings/entities/recurring_list.py

from core.entities.contracts import BaseEntity
from core.schedule.recurrings import selectors


class RecurringListEntity(BaseEntity):
    """
    schedule.recurrings.list entity
    """

    key = "schedule.recurrings.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = selectors.get_recurring_queryset(tenant=tenant)

        search = query.get("search")
        if search:
            qs = qs.filter(event__title__icontains=search)

        qs = qs.order_by("frequency")

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
                "frequency": r.frequency,
                "interval": r.interval,
                "end_date": r.end_date,
            }
            for r in items
        ]

        return {
            "items": data,
            "total": total
        }

