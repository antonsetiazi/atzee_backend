# core/schedule/shifts/entities/shift_select_list.py

from core.entities.contracts import BaseEntity
from core.schedule.shifts import selectors


class ShiftSelectListEntity(BaseEntity):
    """
    schedule.shifts.select.list entity
    """

    key = "schedule.shifts.select.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = selectors.get_shift_queryset(tenant=tenant).order_by(
            "start_datetime"
        )

        items = [
            {
                "value": str(s.id),
                "label": s.name,
            }
            for s in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }

