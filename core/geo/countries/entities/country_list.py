# core/geo/countries/entities/country_list.py

from core.entities.contracts import BaseEntity
from core.geo.countries.models import Country


class CountryListEntity(BaseEntity):
    """
    countries.list entity
    """

    key = "countries.list"
    domain = "core"
    permission = "core.countries.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Country.objects.filter(
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
        items = qs.order_by("name")[offset:limit]

        data = [
            {
                "id": str(c.id),
                "code": c.code,
                "name": c.name,
                "currency_code": c.currency_code,
                "phone_code": c.phone_code,
            }
            for c in items
        ]

        return {
            "items": data,
            "total": total,
        }
