# accounting/models/asset_disposal.py

import uuid

from django.db import models

from accounting.models.fixed_asset import FixedAsset
from accounting.models.journal import Journal
from core.models.base import TenantAwareModel


class AssetDisposal(TenantAwareModel):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("posted", "Posted"),
        ("cancelled", "Cancelled"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    asset = models.ForeignKey(
        FixedAsset,
        on_delete=models.PROTECT,
        related_name="disposals",
    )

    disposal_date = models.DateField()

    disposal_value = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )

    gain_loss_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )

    notes = models.TextField(blank=True)

    journal = models.ForeignKey(
        Journal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="asset_disposals",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    class Meta:
        db_table = "accounting_asset_disposals"

        ordering = [
            "-disposal_date",
            "-created_at",
        ]

    def __str__(self):
        return f"{self.asset.asset_number} " f"- Disposal"
