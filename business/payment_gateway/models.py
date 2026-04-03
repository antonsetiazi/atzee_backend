# business/payment_gateway/models.py

from django.db import models
from core.models.base import TenantAwareModel
from core.tenants.models import Tenant


class PaymentGateway(TenantAwareModel):
    """
    Represent a payment transaction via external gateway (Midtrans, Xendit).
    This is the SOURCE OF TRUTH for payment status.
    """

    STATUS_PENDING = "PENDING"
    STATUS_SUCCESS = "SUCCESS"
    STATUS_FAILED = "FAILED"
    STATUS_EXPIRED = "EXPIRED"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_SUCCESS, "Success"),
        (STATUS_FAILED, "Failed"),
        (STATUS_EXPIRED, "Expired"),
    )

    PROVIDER_MIDTRANS = "midtrans"
    PROVIDER_XENDIT = "xendit"

    PROVIDER_CHOICES = (
        (PROVIDER_MIDTRANS, "Midtrans"),
        (PROVIDER_XENDIT, "Xendit"),
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="gateway_payments"
    )

    # 🔗 Generic reference (order, invoice, etc)
    reference_type = models.CharField(
        max_length=50,
        help_text="order, invoice, subscription, etc"
    )
    reference_id = models.CharField(
        max_length=100,
        help_text="ID of referenced object"
    )

    # 💰 Payment info
    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    currency = models.CharField(
        max_length=10,
        default="IDR"
    )

    # 🌐 Gateway info
    provider = models.CharField(
        max_length=20,
        choices=PROVIDER_CHOICES
    )
    channel = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="gopay, qris, va_bca, etc"
    )

    # 🔑 External identifiers (VERY IMPORTANT)
    external_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Transaction ID from gateway"
    )
    external_reference = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Order ID sent to gateway"
    )

    # 🔗 Payment UI
    payment_url = models.TextField(
        blank=True,
        null=True
    )
    payment_token = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    # 📊 Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    paid_at = models.DateTimeField(
        blank=True,
        null=True
    )
    expired_at = models.DateTimeField(
        blank=True,
        null=True
    )

    # 🧾 Raw payload (for debugging & audit)
    raw_response = models.JSONField(
        blank=True,
        null=True
    )
    raw_webhook = models.JSONField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "payment_gateway_transactions"
        indexes = [
            models.Index(fields=["tenant", "reference_type", "reference_id"]),
            models.Index(fields=["external_id"]),
            models.Index(fields=["status"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.provider} {self.amount} {self.status}"
    

class PaymentMethod(TenantAwareModel):
    """
    Configurable payment channels (GoPay, VA, QRIS, etc)
    Controlled by admin.
    """

    PROVIDER_MIDTRANS = "midtrans"
    PROVIDER_XENDIT = "xendit"

    PROVIDER_CHOICES = (
        (PROVIDER_MIDTRANS, "Midtrans"),
        (PROVIDER_XENDIT, "Xendit"),
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="payment_methods"
    )

    name = models.CharField(
        max_length=100,
        help_text="Display name (GoPay, BCA VA, QRIS)"
    )

    code = models.CharField(
        max_length=50,
        help_text="Internal code (gopay, bca_va, qris)"
    )

    provider = models.CharField(
        max_length=20,
        choices=PROVIDER_CHOICES
    )

    is_active = models.BooleanField(default=True)

    # Optional config per channel
    config = models.JSONField(
        blank=True,
        null=True,
        help_text="Extra config per method (VA prefix, fee, etc)"
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Sorting order in UI"
    )

    class Meta:
        db_table = "payment_gateway_methods"
        unique_together = ("tenant", "code")
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.name} ({self.provider})"    
    

class PaymentGatewayConfig(TenantAwareModel):
    """
    Store API credentials per tenant for each provider.
    """

    PROVIDER_MIDTRANS = "midtrans"
    PROVIDER_XENDIT = "xendit"

    ENV_SANDBOX = "sandbox"
    ENV_PRODUCTION = "production"

    PROVIDER_CHOICES = (
        (PROVIDER_MIDTRANS, "Midtrans"),
        (PROVIDER_XENDIT, "Xendit"),
    )

    ENV_CHOICES = (
        (ENV_SANDBOX, "Sandbox"),
        (ENV_PRODUCTION, "Production"),
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="payment_gateway_configs"
    )

    provider = models.CharField(
        max_length=20,
        choices=PROVIDER_CHOICES
    )

    environment = models.CharField(
        max_length=20,
        choices=ENV_CHOICES,
        default=ENV_SANDBOX
    )

    is_active = models.BooleanField(default=True)

    # 🔐 Credentials
    api_key = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255, blank=True, null=True)

    merchant_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # Flexible config
    extra_config = models.JSONField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "payment_gateway_configs"
        unique_together = ("tenant", "provider")

    def __str__(self):
        return f"{self.tenant_id} - {self.provider} ({self.environment})"    