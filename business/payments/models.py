from django.db import models
from core.models.base import TenantAwareModel
from core.tenants.models import Tenant
from core.users.models import User

class Payment(TenantAwareModel):
    """
    Payment represents a real-world settlement event.
    Immutable business event.
    """

    DIRECTION_IN = "IN"
    DIRECTION_OUT = "OUT"

    DIRECTION_CHOICES = (
        (DIRECTION_IN, "Incoming"),
        (DIRECTION_OUT, "Outgoing"),
    )

    STATUS_DRAFT = "DRAFT"
    STATUS_POSTED = "POSTED"
    STATUS_VOID = "VOID"

    STATUS_CHOICES = (
        (STATUS_DRAFT, "Draft"),
        (STATUS_POSTED, "Posted"),
        (STATUS_VOID, "Void"),
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="business_payments",  # unik
    )

    reference_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="External reference (bank slip, gateway ref, etc)"
    )

    direction = models.CharField(
        max_length=3,
        choices=DIRECTION_CHOICES
    )

    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10,
        default="IDR"
    )

    method = models.CharField(
        max_length=50,
        help_text="cash, transfer, qris, gateway, etc"
    )

    payment_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    # Optional reference
    document_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Referenced document (invoice, bill, etc)"
    )

    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="created_business_payments",  # unik
    )
    updated_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="updated_business_payments",  # unik
    )

    class Meta:
        db_table = "business_payments"
        ordering = ["-payment_date", "-id"]

    def __str__(self):
        return f"{self.direction} {self.amount} {self.currency}"
