# accounting/models/receivable_payment.py

from django.db import models
import uuid
from core.models.base import TenantAwareModel
from business.customers.models import Customer

class ReceivablePayment(TenantAwareModel):

    PAYMENT_METHOD_CHOICES = [
        ("cash", "Cash"),
        ("bank_transfer", "Bank Transfer"),
        ("giro", "Giro"),
        ("other", "Other"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="payments"
    )

    payment_number = models.CharField(max_length=100)

    payment_date = models.DateField()

    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHOD_CHOICES,
        default="bank_transfer"
    )

    reference = models.CharField(
        max_length=100,
        blank=True
    )

    notes = models.TextField(blank=True)

    class Meta:
        db_table = "accounting_receivable_payments"
        ordering = ["-payment_date"]

    def __str__(self):
        return self.payment_number