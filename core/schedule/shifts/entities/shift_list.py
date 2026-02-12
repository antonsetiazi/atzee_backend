# core/schedule/shifts/entities/shift_list.py

from core.entities.contracts import BaseEntity
from core.schedule.shifts.models import Shift


class ShiftListEntity(BaseEntity):
    """
    shifts.list entity
    """

    key = "schedule.shifts.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Shift.objects.filter(tenant=tenant, is_deleted=False)

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        qs = qs.order_by("start_time")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))
        offset = (page - 1) * page_size
        limit = offset + page_size
        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(s.id),
                "name": s.name,
                "start_time": s.start_time,
                "end_time": s.end_time,
            }
            for s in items
        ]
        return {"items": data, "total": total}
