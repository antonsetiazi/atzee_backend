# accounting/models/receivable_invoice_item.py

from django.db import models
import uuid
from decimal import Decimal
from core.models.base import TenantAwareModel


class ReceivableInvoiceItem(TenantAwareModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    invoice = models.ForeignKey(
        "accounting.ReceivableInvoice",
        on_delete=models.CASCADE,
        related_name="items"
    )

    description = models.CharField(max_length=255)

    qty = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=1
    )

    unit_price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    total = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    class Meta:
        db_table = "accounting_receivable_invoice_items"

    def save(self, *args, **kwargs):

        self.total = (
            Decimal(self.qty) *
            Decimal(self.unit_price)
        )

        super().save(*args, **kwargs)