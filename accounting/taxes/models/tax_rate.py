# accounting/taxes/models/tax_rate.py

from django.db import models
from core.models.base import TenantAwareModel
from accounting.taxes.models.tax import Tax


class TaxRate(TenantAwareModel):
    """
    Tax rate versioning.
    Handles historical & future changes.
    """

    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, related_name="rates")
    
    rate = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        help_text="Percentage value, e.g. 11.0000"
    )

    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "accounting_tax_rate"
        unique_together = ("tenant", "tax", "effective_from")
        ordering = ("-effective_from",)

    def __str__(self):
        return f"{self.tax.code} @ {self.rate}%"
