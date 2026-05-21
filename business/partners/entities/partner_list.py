# business/partners/entities/partner_list.py

from business.partners.models import Partner
from core.entities.contracts import BaseEntity


class PartnerListEntity(BaseEntity):
    key = "partners.list"
    domain = "business"
    permission = "business.partners.view"

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = (
            Partner.objects.filter(
                tenant=tenant,
                is_deleted=False,
            )
            # 🔥 OPTIMIZE FK (hindari N+1)
            .select_related("city", "region")
        )

        # 🔍 SEARCH
        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 1000))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        # 🔁 SERIALIZE (FULL for UI)
        data = []
        for c in items:
            data.append(
                {
                    "id": str(c.id),
                    "code": c.code or "-",
                    "name": c.name,
                    "phone": c.phone or "-",
                    "email": c.email or "-",
                    # 🔥 LOCATION
                    "city_name": c.city.name if c.city else "-",
                    # 🔥 BUSINESS METRICS
                    "base_price": float(c.base_price) if c.base_price else 0,
                    "rating_avg": float(c.rating_avg or 0),
                    "rating_count": c.rating_count or 0,
                    # 🔥 STATUS (fallback dari meta)
                    "is_active": c.meta.get("is_active", True),
                }
            )

        return {
            "items": data,
            "total": total,
        }
