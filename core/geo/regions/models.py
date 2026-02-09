# core/geo/regions/models.py

from django.db import models
from core.models.base import TenantAwareModel
from core.geo.countries.models import Country


class Region(TenantAwareModel):
    """
    Administrative region.
    Example: Jawa Barat, California
    """

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="regions"
    )

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_regions"
        unique_together = ("tenant", "country", "code")
        ordering = ["name"]

    def __str__(self):
        return self.name
