# core/geo/cities/models.py

from django.db import models
from core.models.base import GlobalMasterModel
from core.geo.countries.models import Country
from core.geo.regions.models import Region


class City(GlobalMasterModel):
    """
    City / Regency master.
    Example:
    - Kota Bandung
    - Kabupaten Garut
    """

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="cities"
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="cities"
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
        db_table = "core_cities"
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["region", "code"],
                name="uniq_city_region_code"
            )
        ]

        indexes = [
            models.Index(fields=["country", "region"]),
            models.Index(fields=["code"]),
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name