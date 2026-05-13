# accounting/models/fixed_asset.py

import uuid

from django.db import models

from accounting.models.asset_category import (
    AssetCategory,
)
from core.models.base import TenantAwareModel


class FixedAsset(TenantAwareModel):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("active", "Active"),
        ("fully_depreciated", "Fully Depreciated"),
        ("disposed", "Disposed"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    asset_number = models.CharField(
        max_length=100,
    )

    name = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    category = models.ForeignKey(
        AssetCategory,
        on_delete=models.PROTECT,
        related_name="assets",
    )

    serial_number = models.CharField(
        max_length=255,
        blank=True,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    # =========================================================
    # ACQUISITION
    # =========================================================

    purchase_date = models.DateField()

    capitalization_date = models.DateField()

    purchase_cost = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    salvage_value = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )

    # =========================================================
    # DEPRECIATION
    # =========================================================

    depreciation_method = models.CharField(
        max_length=50,
    )

    useful_life_months = models.PositiveIntegerField()

    depreciation_start_date = models.DateField()

    last_depreciation_date = models.DateField(
        null=True,
        blank=True,
    )

    accumulated_depreciation = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )

    book_value = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )

    # =========================================================
    # STATUS
    # =========================================================

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="draft",
    )

    class Meta:
        db_table = "accounting_fixed_assets"

        ordering = [
            "-capitalization_date",
            "asset_number",
        ]

        unique_together = (
            "tenant",
            "asset_number",
        )

    def __str__(self):
        return f"{self.asset_number} - {self.name}"
