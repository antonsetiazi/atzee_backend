# business/transactions/reference_generators/__init__.py

from business.transactions.models.enums import TransactionType
from .registry import TransactionReferenceRegistry
from .sales import generate_sales_reference

TransactionReferenceRegistry.register(
    TransactionType.SALES,
    generate_sales_reference,
)