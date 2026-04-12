# core/geo/regions/models.py

from django.db import models
from core.models.base import GlobalMasterModel
from core.geo.countries.models import Country


class Region(GlobalMasterModel):
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
    center_latitude = models.FloatField(null=True, blank=True)
    center_longitude = models.FloatField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_regions"
        constraints = [
            models.UniqueConstraint(
                fields=["country", "code"],
                name="uniq_region_country_code"
            )
        ]
        ordering = ["name"]
    def __str__(self):
        return self.name
