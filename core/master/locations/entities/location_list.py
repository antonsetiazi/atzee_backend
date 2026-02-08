# core/master/locations/entities/location_list.py

from core.entities.contracts import BaseEntity
from core.master.locations.models import Location


class LocationListEntity(BaseEntity):
    """
    location.list entity
    """

    key = "locations.list"
    domain = "core"
    permission = "core.location.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Location.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).select_related("parent")

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
                "id": str(loc.id),
                "code": loc.code,
                "name": loc.name,
                "parent_name": loc.parent.name if loc.parent else None,
                "is_active": loc.is_active,
            }
            for loc in items
        ]

        return {
            "items": data,
            "total": total,
        }
