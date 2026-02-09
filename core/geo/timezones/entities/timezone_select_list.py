# core/geo/timezones/entities/timezone_select_list.py

from core.entities.contracts import BaseEntity
from core.geo.timezones.models import Timezone


class TimezoneSelectListEntity(BaseEntity):
    """
    timezones.select.list entity
    """

    key = "timezones.select.list"
    domain = "core"
    permission = "core.timezones.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Timezone.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).order_by("name")

        items = [
            {
                "value": str(t.id),
                "label": f"{t.name} ({t.utc_offset})",
            }
            for t in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
