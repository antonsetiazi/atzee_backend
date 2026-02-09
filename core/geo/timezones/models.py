# core/geo/timezones/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Timezone(TenantAwareModel):
    """
    Timezone master.
    Example: Asia/Jakarta, UTC
    """

    name = models.CharField(max_length=100)
    utc_offset = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_timezones"
        unique_together = ("tenant", "name")
        ordering = ["name"]

    def __str__(self):
        return self.name
