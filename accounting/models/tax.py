# accounting/models/tax.py

from django.db import models
import uuid

from core.models.base import (
    TenantAwareModel
)


class Tax(
    TenantAwareModel
):

    TAX_TYPE_CHOICES = [
        ("sales", "Sales Tax"),
        ("purchase", "Purchase Tax"),
        ("withholding", "Withholding Tax"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    code = models.CharField(
        max_length=50
    )

    name = models.CharField(
        max_length=255
    )

    tax_type = models.CharField(
        max_length=30,
        choices=TAX_TYPE_CHOICES
    )

    rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    sales_account = models.ForeignKey(
        "accounting.Account",
        on_delete=models.PROTECT,
        related_name="sales_tax_configs",
        null=True,
        blank=True
    )

    purchase_account = models.ForeignKey(
        "accounting.Account",
        on_delete=models.PROTECT,
        related_name="purchase_tax_configs",
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "accounting_taxes"

        ordering = ["name"]

        unique_together = (
            "tenant",
            "code",
        )

    def __str__(self):
        return f"{self.name} ({self.rate}%)"