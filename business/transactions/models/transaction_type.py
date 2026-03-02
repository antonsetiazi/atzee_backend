# business/transactions/models/transaction_type.py

from django.db import models
from core.models.base import TenantAwareModel

from business.transactions.models.enums import TransactionDirection


class TransactionType(TenantAwareModel):
    """
    Configurable transaction type.
    Per-tenant.
    Drives behavior of transaction engine.
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    direction = models.CharField(
        max_length=20,
        choices=TransactionDirection.choices
    )

    # Behavior flags
    require_customer = models.BooleanField(default=False)
    require_partner = models.BooleanField(default=False)
    affect_stock = models.BooleanField(default=True)
    auto_post = models.BooleanField(default=False)
    allow_anonymous = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "business_transaction_types"
        unique_together = ("tenant", "code")
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"