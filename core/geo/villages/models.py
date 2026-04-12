# core/geo/villages/models.py

from django.db import models
from core.models.base import GlobalMasterModel
from core.geo.countries.models import Country
from core.geo.regions.models import Region
from core.geo.cities.models import City
from core.geo.districts.models import District


class Village(GlobalMasterModel):
    """
    Village / Kelurahan / Desa master.
    Example:
    - Dago
    - Cipaganti
    """

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="villages"
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="villages"
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="villages"
    )

    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name="villages"
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
        db_table = "core_villages"
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["district", "code"],
                name="uniq_village_district_code"
            )
        ]

        indexes = [
            models.Index(fields=["country", "region", "city", "district"]),
            models.Index(fields=["code"]),
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name