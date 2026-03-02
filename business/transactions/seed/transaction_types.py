# business/transactions/seed/transaction_types.py

from business.transactions.models.transaction_type import TransactionType


DEFAULT_TRANSACTION_TYPES = [
    {
        "code": "sales",
        "name": "Sales",
        "direction": "out",
        "require_customer": True,
        "require_partner": False,
        "affect_stock": True,
    },
    {
        "code": "purchase",
        "name": "Purchase",
        "direction": "in",
        "require_customer": False,
        "require_partner": True,
        "affect_stock": True,
    },
    {
        "code": "adjustment",
        "name": "Stock Adjustment",
        "direction": "internal",
        "require_customer": False,
        "require_partner": False,
        "affect_stock": True,
    },
    {
        "code": "transfer",
        "name": "Stock Transfer",
        "direction": "internal",
        "require_customer": False,
        "require_partner": False,
        "affect_stock": True,
    },
]


def seed_transaction_types(tenant):
    for data in DEFAULT_TRANSACTION_TYPES:
        TransactionType.objects.update_or_create(
            tenant=tenant,
            code=data["code"],
            defaults=data,
        )