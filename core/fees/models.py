# core/fees/models.py

import uuid
from django.db import models

from core.models.base import TenantAwareModel
from business.partners.models import Partner
from core.classifications.categories.models import Category
from marketplace.models.order import Order


class FeeConfig(TenantAwareModel):
    """
    Master konfigurasi fee (tenant-scoped)
    """

    FEE_TYPE_CHOICES = (
        ("percent", "Percent"),
        ("fixed", "Fixed"),
    )

    APPLIES_TO_CHOICES = (
        ("customer", "Customer"),
        ("partner", "Partner"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100)

    fee_type = models.CharField(
        max_length=20,
        choices=FEE_TYPE_CHOICES
    )

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Percent (0-100) atau nominal fixed"
    )

    applies_to = models.CharField(
        max_length=20,
        choices=APPLIES_TO_CHOICES
    )

    # =========================
    # RELATIONAL FILTER (BETTER)
    # =========================
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="fee_configs"
    )

    partner = models.ForeignKey(
        Partner,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="fee_configs"
    )

    # =========================
    # RANGE FILTER
    # =========================
    min_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    max_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_fee_configs"
        indexes = [
            models.Index(fields=["tenant", "is_active"]),
            models.Index(fields=["tenant", "category"]),
            models.Index(fields=["tenant", "partner"]),
        ]

    def __str__(self):
        return f"{self.name}"
    

class OrderFee(models.Model):
    """
    Snapshot fee saat transaksi terjadi
    (IMMUTABLE - finance critical)
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="fees"
    )

    # =========================
    # SNAPSHOT DATA (JANGAN FK)
    # =========================
    fee_name = models.CharField(max_length=100)
    fee_type = models.CharField(max_length=20)
    applies_to = models.CharField(max_length=20)

    value = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    # optional metadata snapshot
    meta = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "core_order_fees"
        indexes = [
            models.Index(fields=["order"]),
        ]    