# core/schedule/holidays/entities/holiday_list.py

from core.entities.contracts import BaseEntity
from core.schedule.holidays.models import Holiday


class HolidayListEntity(BaseEntity):
    """
    holidays.list entity
    """

    key = "schedule.holidays.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Holiday.objects.filter(tenant=tenant, is_deleted=False)

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        qs = qs.order_by("start_datetime")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))
        offset = (page - 1) * page_size
        limit = offset + page_size
        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(h.id),
                "name": h.name,
                "start_datetime": h.start_datetime.isoformat() if h.start_datetime else None,
                "end_datetime": h.end_datetime.isoformat() if h.end_datetime else None,
                "recurring": h.recurring,
                "all_day": h.all_day,
            }
            for h in items
        ]

        return {"items": data, "total": total}

