# accounting/models/asset_category.py

import uuid
from decimal import Decimal

from django.db import models

from accounting.enum.depreciation_method import (
    DepreciationMethod,
)
from accounting.models.account import Account
from core.models.base import TenantAwareModel


class AssetCategory(TenantAwareModel):
    """
    Asset category configuration.
    Menjadi template default untuk fixed asset.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(max_length=255)

    code = models.CharField(max_length=50)

    description = models.TextField(
        blank=True,
        null=True,
    )

    # =========================================================
    # ACCOUNT CONFIGURATION
    # =========================================================

    asset_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="asset_category_asset_accounts",
    )

    accumulated_depreciation_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="asset_category_accumulated_accounts",
    )

    depreciation_expense_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="asset_category_expense_accounts",
    )

    # =========================================================
    # DEPRECIATION
    # =========================================================

    depreciation_method = models.CharField(
        max_length=50,
        choices=DepreciationMethod.choices,
        default=DepreciationMethod.STRAIGHT_LINE,
    )

    useful_life_months = models.PositiveIntegerField(
        default=12,
    )

    salvage_value_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    class Meta:
        db_table = "accounting_asset_categories"
        unique_together = ("tenant", "code")
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"
