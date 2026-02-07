# accounting/fiscal_period/entities/fiscal_period_list.py

from core.entities.contracts import BaseEntity
from accounting.fiscal_period.models import FiscalPeriod
from django.utils import timezone


class FiscalPeriodListEntity(BaseEntity):
    """
    fiscal_period.list entity
    """

    key = "fiscal_period.list"
    domain = "accounting"
    permission = "accounting.fiscal_period.view"

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

        qs = FiscalPeriod.objects.filter(
            tenant=tenant,
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

        # 🔁 SERIALIZE
        data = [
            {
                "id": str(p.id),
                "name": p.name,
                "start_date": p.start_date.isoformat(),
                "end_date": p.end_date.isoformat(),
                "is_closed": p.is_closed,
                "closed_at": p.closed_at.isoformat() if p.closed_at else None,
                "closed_by": str(p.closed_by.id) if p.closed_by else None,
            }
            for p in items
        ]

        return {
            "items": data,
            "total": total,
        }
