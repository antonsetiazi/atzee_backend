# core/geo/regions/entities/region_select_list.py

from core.entities.contracts import BaseEntity
from core.geo.regions.models import Region


class RegionSelectListEntity(BaseEntity):
    """
    regions.select.list entity
    """

    key = "regions.select.list"
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

        items = [
            {
                "value": str(r.id),
                "label": f"{r.name} ({r.country.code})",
            }
            for r in qs.order_by("name")
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
