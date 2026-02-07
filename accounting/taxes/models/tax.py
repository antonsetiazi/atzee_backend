# accounting/taxes/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Tax(TenantAwareModel):
    """
    Tax master definition.
    Example:
    - VAT / PPN
    - Withholding Tax
    - Service Tax
    """

    code = models.CharField(
        max_length=30,
        help_text="Unique tax code, e.g. VAT_ID, PPH_23"
    )
    name = models.CharField(max_length=100)

    TYPE_CHOICES = (
        ("percentage", "Percentage"),
        ("fixed", "Fixed"),
        ("withholding", "Withholding"),
    )
    type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES,
        null=True,
        blank=True
    )

    SCOPE_CHOICES = (
        ("sales", "Sales"),
        ("purchase", "Purchase"),
        ("both", "Both"),
    )
    scope = models.CharField(
        max_length=20, 
        choices=SCOPE_CHOICES,
        null=True,
        blank=True
    )

    recoverable = models.BooleanField(
        default=False,
        help_text="Can this tax be reclaimed? (e.g. VAT Input)"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "accounting_tax"
        unique_together = ("tenant", "code")

    def __str__(self):
        return f"{self.code} - {self.name}"