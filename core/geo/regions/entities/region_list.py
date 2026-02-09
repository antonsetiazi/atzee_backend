# core/geo/regions/entities/region_list.py

from core.entities.contracts import BaseEntity
from core.geo.regions.models import Region


class RegionListEntity(BaseEntity):
    """
    regions.list entity
    """

    key = "regions.list"
    domain = "core"
    permission = "core.regions.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Region.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).select_related("country")

        country_id = query.get("country_id")
        if country_id:
            qs = qs.filter(country_id=country_id)

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("name")[offset:limit]

        data = [
            {
                "id": str(r.id),
                "code": r.code,
                "name": r.name,
                "country": r.country.name,
                "country_id": str(r.country_id),
            }
            for r in items
        ]

        return {
            "items": data,
            "total": total,
        }
