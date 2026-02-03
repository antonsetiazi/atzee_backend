# business/sales/entities/sales_direct_items.py

from core.entities.contracts import BaseEntity
from business.transactions.selectors import get_transaction_by_id
from django.core.exceptions import ValidationError


class SalesDirectItemsEntity(BaseEntity):
    """
    sales.direct.items
    Line items for direct sales transaction
    """

    key = "sales.direct.items"
    domain = "business"
    permission = "business.sales.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        transaction_id = query.get("id")
        if not transaction_id:
            raise ValidationError("Transaction ID is required")

        trx = get_transaction_by_id(
            tenant=tenant,
            transaction_id=transaction_id,
        )

        if not trx:
            raise ValidationError("Transaction not found")

        items = [
            {
                "id": item.id,
                "parent_id": trx.id,
                "product_id": item.product.id,
                "product_name": item.product.name,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
                "total_price": item.total_price,
                "notes": item.notes,
            }
            for item in trx.items.all()
        ]

        return {
            "items": items,
            "total": len(items),
        }
