# core/master/currencies/entities/currency_list.py

from core.entities.contracts import BaseEntity
from core.master.currencies.models import Currency


class CurrencyListEntity(BaseEntity):
    """
    currencies.list entity
    """

    key = "currencies.list"
    domain = "core"
    permission = "core.currencies.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Currency.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        )

        search = query.get("search")
        if search:
            qs = qs.filter(
                code__icontains=search
            ) | qs.filter(
                name__icontains=search
            )

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("code")[offset:limit]

        data = [
            {
                "id": str(c.id),
                "code": c.code,
                "name": c.name,
                "symbol": c.symbol,
            }
            for c in items
        ]

        return {
            "items": data,
            "total": total,
        }
