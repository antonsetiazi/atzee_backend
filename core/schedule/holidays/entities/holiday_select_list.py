# core/schedule/holidays/entities/holiday_select_list.py

from core.entities.contracts import BaseEntity
from core.schedule.holidays.models import Holiday


class HolidaySelectListEntity(BaseEntity):
    """
    holidays.select.list entity
    """

    key = "schedule.holidays.select.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Holiday.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).order_by("date")

        items = [
            {
                "value": str(h.id),
                "label": h.name,
            }
            for h in qs
        ]

        return {"items": items, "total": qs.count()}
