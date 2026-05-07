# accounting/models/receivable_allocation.py

from django.db import models
import uuid
from core.models.base import TenantAwareModel


class ReceivableAllocation(TenantAwareModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    payment = models.ForeignKey(
        "accounting.ReceivablePayment",
        on_delete=models.CASCADE,
        related_name="allocations"
    )

    invoice = models.ForeignKey(
        "accounting.ReceivableInvoice",
        on_delete=models.CASCADE,
        related_name="allocations"
    )

    allocated_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )

    class Meta:
        db_table = "accounting_receivable_allocations"