# core/geo/countries/entities/country_select_list.py

from core.entities.contracts import BaseEntity
from core.geo.countries.models import Country


class CountrySelectListEntity(BaseEntity):
    """
    countries.select.list entity
    """

    key = "countries.select.list"
    domain = "core"
    permission = "core.countries.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Country.objects.filter(
            tenant=tenant,
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
