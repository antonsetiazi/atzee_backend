# core/master/uom/models.py

from django.db import models
from core.models.base import TenantAwareModel


class UOMCategory(TenantAwareModel):
    """
    Category of unit of measure.
    Example: LENGTH, WEIGHT, VOLUME
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "core_uom_categories"
        unique_together = ("tenant", "code")
        ordering = ["name"]

    def __str__(self):
        return self.name


class UOM(TenantAwareModel):
    """
    Unit of Measure.
    Example: kg, g, pcs
    """

    category = models.ForeignKey(
        UOMCategory,
        on_delete=models.PROTECT,
        related_name="uoms"
    )

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, blank=True)

    is_base = models.BooleanField(default=False)
    precision = models.PositiveSmallIntegerField(default=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_uoms"
        unique_together = (
            ("tenant", "code"),
            ("tenant", "category", "name"),
        )
        ordering = ["name"]

    def __str__(self):
        return self.code


class UOMConversion(TenantAwareModel):
    """
    Conversion rule between units in same category.
    """

    from_uom = models.ForeignKey(
        UOM,
        on_delete=models.CASCADE,
        related_name="conversions_from"
    )
    to_uom = models.ForeignKey(
        UOM,
        on_delete=models.CASCADE,
        related_name="conversions_to"
    )

    factor = models.DecimalField(
        max_digits=20,
        decimal_places=8
    )

    class Meta:
        db_table = "core_uom_conversions"
        unique_together = ("tenant", "from_uom", "to_uom")

    def clean(self):
        if self.from_uom.category_id != self.to_uom.category_id:
            raise ValueError("UOM conversion must be in same category")
