# accounting/models/payable_invoice.py

from django.db import models
import uuid
from decimal import Decimal

from core.models.base import (
    TenantAwareModel
)

from business.partners.models import Partner


class PayableInvoice(TenantAwareModel):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("posted", "Posted"),
        ("partial", "Partial"),
        ("paid", "Paid"),
        ("cancelled", "Cancelled"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    partner = models.ForeignKey(
        Partner,
        on_delete=models.PROTECT,
        related_name="payable_invoices"
    )

    invoice_number = models.CharField(
        max_length=100
    )

    invoice_date = models.DateField()

    due_date = models.DateField()

    notes = models.TextField(blank=True)

    tax = models.ForeignKey(
        "accounting.Tax",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payable_invoices"
    )

    subtotal = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    tax_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    paid_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    balance_due = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    class Meta:
        db_table = "accounting_payable_invoices"

        ordering = [
            "-invoice_date"
        ]

    def __str__(self):
        return self.invoice_number


    def refresh_payment_status(self):

        self.balance_due = (
            Decimal(self.total_amount) -
            Decimal(self.paid_amount)
        )

        if self.paid_amount <= 0:

            self.status = "posted"

        elif self.balance_due > 0:

            self.status = "partial"

        else:

            self.status = "paid"

        self.save(
            update_fields=[
                "paid_amount",
                "balance_due",
                "status",
            ]
        )