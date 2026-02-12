# core/schedule/shifts/entities/shift_list.py

from core.entities.contracts import BaseEntity
from core.schedule.shifts import selectors


class ShiftListEntity(BaseEntity):
    """
    schedule.shifts.list entity
    """

    key = "schedule.shifts.list"
    domain = "core"
    permission = "core.schedule.view"

    MAX_PAGE_SIZE = 100

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = selectors.get_shift_queryset(tenant=tenant)

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        qs = qs.order_by("start_datetime")

        page = max(int(query.get("page", 1)), 1)
        page_size = min(
            max(int(query.get("pageSize", 10)), 1),
            self.MAX_PAGE_SIZE,
        )

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(s.id),
                "name": s.name,
                "start_datetime": s.start_datetime,
                "end_datetime": s.end_datetime,
            }
            for s in items
        ]

        return {
            "items": data,
            "total": total,
        }
