# core/schedule/events/entities/event_list.py

from core.entities.contracts import BaseEntity
from core.schedule.events.models import Event


class EventListEntity(BaseEntity):
    """
    events.list entity
    """

    key = "schedule.events.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Event.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).select_related("created_by")

        # filters
        start_date = query.get("start_date")
        if start_date:
            qs = qs.filter(start_datetime__gte=start_date)
        end_date = query.get("end_date")
        if end_date:
            qs = qs.filter(end_datetime__lte=end_date)

        search = query.get("search")
        if search:
            qs = qs.filter(title__icontains=search)

        qs = qs.order_by("start_datetime")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(e.id),
                "title": e.title,
                "start_datetime": e.start_datetime,
                "end_datetime": e.end_datetime,
                "all_day": e.all_day,
                "created_by": e.created_by.full_name if e.created_by else None,
            }
            for e in items
        ]

        return {"items": data, "total": total}
