# core/geo/timezones/entities/timezone_list.py

from core.entities.contracts import BaseEntity
from core.geo.timezones.models import Timezone


class TimezoneListEntity(BaseEntity):
    """
    timezones.list entity
    """

    key = "timezones.list"
    domain = "core"
    permission = "core.timezones.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Timezone.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        )

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(t.id),
                "name": t.name,
                "utc_offset": t.utc_offset,
            }
            for t in items
        ]

        return {
            "items": data,
            "total": total,
        }
