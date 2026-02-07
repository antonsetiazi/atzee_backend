# accounting/taxes/models/tax_rule.py

from django.db import models
from core.models.base import TenantAwareModel
from .tax import Tax


class TaxRule(TenantAwareModel):
    """
    Defines WHEN a tax applies.
    """

    name = models.CharField(max_length=100)

    tax = models.ForeignKey(
        Tax,
        on_delete=models.CASCADE,
        related_name="rules"
    )

    EVENT_CHOICES = (
        ("sales", "Sales"),
        ("purchase", "Purchase"),
    )
    event = models.CharField(
        max_length=20,
        choices=EVENT_CHOICES
    )

    priority = models.PositiveIntegerField(
        default=100,
        help_text="Lower number = higher priority"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "accounting_tax_rule"
        ordering = ("priority",)

    def __str__(self):
        return f"{self.name} ({self.tax.code})"
