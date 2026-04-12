# core/geo/districts/models.py

from django.db import models
from core.models.base import GlobalMasterModel
from core.geo.countries.models import Country
from core.geo.regions.models import Region
from core.geo.cities.models import City


class District(GlobalMasterModel):
    """
    District / Kecamatan master.
    Example:
    - Coblong
    - Cidadap
    """

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="districts"
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="districts"
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="districts"
    )

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    center_latitude = models.FloatField(
        null=True,
        blank=True
    )

    center_longitude = models.FloatField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "core_districts"
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["city", "code"],
                name="uniq_district_city_code"
            )
        ]

        indexes = [
            models.Index(fields=["country", "region", "city"]),
            models.Index(fields=["code"]),
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name