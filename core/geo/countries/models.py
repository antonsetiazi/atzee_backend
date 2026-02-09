# core/geo/countries/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Country(TenantAwareModel):
    """
    Country master (ISO 3166-1).
    Example: ID, US, JP
    """

    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    phone_code = models.CharField(max_length=10, blank=True)
    currency_code = models.CharField(max_length=10, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_countries"
        unique_together = ("tenant", "code")
        ordering = ["name"]

    def __str__(self):
        return self.name
