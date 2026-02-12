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

        qs = qs.order_by("date")

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
                "date": h.date,
                "is_recurring": h.is_recurring,
            }
            for h in items
        ]
        return {"items": data, "total": total}
