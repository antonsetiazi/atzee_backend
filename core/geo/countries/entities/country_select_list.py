# core/geo/countries/entities/country_select_list.py

from core.entities.contracts import BaseEntity
from core.geo.countries.models import Country

from core.enum.permissions import CorePermission

class CountrySelectListEntity(BaseEntity):
    """
    countries.select.list entity
    """

    key = "countries.select.list"
    domain = "core"
    permission = CorePermission.COUNTRIES_SELECT_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Country.objects.filter(
            is_deleted=False,
            is_active=True,
        ).order_by("name")

        items = [
            {
                "value": str(c.id),
                "label": c.name,
            }
            for c in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
