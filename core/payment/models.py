# core/payment/models.py

from django.db import models
from django.core.exceptions import ValidationError
from core.models.base import TenantAwareModel
from core.users.models import User
from core.tenants.models import Tenant


class PaymentStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PENDING = "PENDING", "Pending"
    SUCCESS = "SUCCESS", "Success"
    FAILED = "FAILED", "Failed"
    CANCELLED = "CANCELLED", "Cancelled"


class PaymentGatewayType(models.TextChoices):
    WALLET = "WALLET", "Internal Wallet"
    MIDTRANS = "MIDTRANS", "Midtrans"
    XENDIT = "XENDIT", "Xendit"

    
class PaymentMethod(TenantAwareModel):
    """
    Core Payment Method
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    gateway = models.CharField(
        max_length=20,
        choices=PaymentGatewayType.choices,
        default=PaymentGatewayType.WALLET,
    )
    
    class Meta:
        db_table = "core_payment_methods"
        unique_together = ("tenant", "code")

    def __str__(self):
        return self.name


class Payment(TenantAwareModel):
    """
    General payment record
    """
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="core_payments",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.PROTECT,
        related_name="payments"
    )

    amount = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.DRAFT
    )

    # optional reference to domain entity, e.g. booking.id
    reference = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, default="")

    external_id = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text="Transaction ID from payment gateway"
    )

    gateway_response = models.JSONField(
        blank=True,
        null=True,
        help_text="Raw response from payment gateway"
    )

    client_payload = models.JSONField(
        blank=True,
        null=True,
        help_text="Data needed by frontend (redirect_url, snap_token, qr_string, etc)"
    )
        
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="created_core_payments",  # unik
    )
    updated_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="updated_core_payments",  # unik
    )
    
    class Meta:
        db_table = "core_payments"
        indexes = [
            models.Index(fields=["tenant", "user", "status"]),
        ]

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Payment amount must be positive.")