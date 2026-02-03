# business/partners/entities/partner_list.py

from core.entities.contracts import BaseEntity
from business.partners.models import Partner


class PartnerListEntity(BaseEntity):
    """
    partners.list entity
    """

    key = "partners.list"
    domain = "business"
    permission = "business.partners.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format (from frontend):
        {
            page: 1,
            pageSize: 10,
            search?: str,
            filters?: {},
            sort?: {}
        }
        """

        qs = Partner.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        # 🔍 SEARCH
        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()

        items = qs[offset:limit]

        # 🔁 SERIALIZE (simple & explicit)
        data = [
            {
                "id": str(c.id),
                "code": c.code,
                "name": c.name,
                "phone": c.phone,
                "email": c.email,
            }
            for c in items
        ]

        return {
            "items": data,
            "total": total,
        }
