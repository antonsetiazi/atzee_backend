# core/schedule/shifts/entities/shift_select_list.py

from core.entities.contracts import BaseEntity
from core.schedule.shifts.models import Shift


class ShiftSelectListEntity(BaseEntity):
    """
    shifts.select.list entity
    """

    key = "schedule.shifts.select.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Shift.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).order_by("start_time")

        items = [
            {
                "value": str(s.id),
                "label": s.name,
            }
            for s in qs
        ]

        return {"items": items, "total": qs.count()}
