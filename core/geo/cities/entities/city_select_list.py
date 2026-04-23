# core/geo/cities/entities/city_select_list.py

from core.entities.contracts import BaseEntity
from core.geo.cities.models import City

from core.enum.permissions import CorePermission


class CitySelectListEntity(BaseEntity):
    key = "cities.select.list"
    domain = "core"
    permission = CorePermission.CITIES_SELECT_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:
        region_id = query.get("region_id")

        qs = City.objects.filter(
            is_deleted=False,
            is_active=True,
        )

        if region_id:
            qs = qs.filter(region_id=region_id)

        qs = qs.order_by("name")

        return {
            "items": [
                {
                    "value": str(obj.id),
                    "label": obj.name,
                }
                for obj in qs
            ],
            "total": qs.count(),
        }
