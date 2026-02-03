from core.entities.contracts import BaseEntity
from business.transactions.selectors import get_transactions_by_type
from business.transactions.models.enums import (
    TransactionType,
    TransactionSubType,
)


class SalesDirectListEntity(BaseEntity):
    """
    sales.direct.list
    Projection of Transaction where:
    - type = SALES
    - subtype = DIRECT
    """

    key = "sales.direct.list"
    domain = "business"
    permission = "business.sales.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = (
            get_transactions_by_type(
                tenant=tenant,
                transaction_type=TransactionType.SALES,
            )
            .filter(subtype=TransactionSubType.DIRECT)
        )

        # 🔍 SEARCH (by reference)
        search = query.get("search")
        if search:
            qs = qs.filter(reference__icontains=search)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(trx.id),
                "reference": trx.reference,
                "transaction_date": trx.transaction_date,
                "notes": trx.notes,
                "status": trx.status,
                "total_items": trx.items.count(),
            }
            for trx in items
        ]

        return {
            "items": data,
            "total": total,
        }
