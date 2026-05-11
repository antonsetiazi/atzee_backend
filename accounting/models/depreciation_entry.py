# accounting/models/depreciation_entry.py

import uuid

from django.db import models

from accounting.models.fixed_asset import FixedAsset
from accounting.models.journal import Journal
from core.models.base import TenantAwareModel


class DepreciationEntry(TenantAwareModel):

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
        related_name="depreciation_entries",
    )

    period_date = models.DateField()

    depreciation_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    accumulated_depreciation = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    book_value_after = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    journal = models.ForeignKey(
        Journal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="depreciation_entries",
    )

    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    class Meta:
        db_table = "accounting_depreciation_entries"

        ordering = [
            "-period_date",
            "-created_at",
        ]

    def __str__(self):
        return f"{self.asset.asset_number} " f"- {self.period_date}"
