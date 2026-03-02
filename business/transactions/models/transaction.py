# business/transactions/models/transaction.py

from django.db import models
from core.models.base import TenantAwareModel

from business.customers.models import Customer
from business.partners.models import Partner
from business.transactions.models.enums import (
    TransactionSubType,
    TransactionStatus
)

from business.transactions.models.transaction_type import TransactionType

class Transaction(TenantAwareModel):
    """
    Business Transaction (aggregate root).
    """

    reference = models.CharField(
        max_length=100,
        help_text="Human readable transaction number"
    )

    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.PROTECT,
        related_name="transactions"
    )

    subtype = models.CharField(
        max_length=30,
        choices=TransactionSubType.choices,
        blank=True,
        null=True,
        help_text="Business flow subtype"
    )

    
    status = models.CharField(
        max_length=20,
        choices=TransactionStatus.choices,
        default=TransactionStatus.DRAFT
    )

    customer = models.ForeignKey(
        Customer,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="transactions"
    )

    partner = models.ForeignKey(
        Partner,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="transactions"
    )

    transaction_date = models.DateField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "business_transactions"
        ordering = ["-transaction_date"]
        unique_together = ("tenant", "reference")

    def __str__(self):
        return f"{self.reference} ({self.transaction_type})"