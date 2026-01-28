from django.db import models

from shared.models import TenantAwareModel
from business.products.models import Product
from business.transactions.models.transaction import Transaction


class TransactionItem(TenantAwareModel):
    """
    Line item inside transaction.
    """

    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.DecimalField(
        max_digits=14,
        decimal_places=4
    )

    unit_price = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    total_price = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "business_transaction_items"
        ordering = ["id"]
        unique_together = ("transaction", "product")

    
    def __str__(self):
        return f"{self.product} x {self.quantity}"