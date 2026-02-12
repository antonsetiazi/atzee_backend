# core/schedule/holidays/models.py

from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel


class Holiday(TenantAwareModel, ExtensibleModel):
    """
    Holiday / blackout period
    """

    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    all_day = models.BooleanField(default=True)
    recurring = models.BooleanField(default=False)

    metadata = models.JSONField(
        blank=True,
        null=True,
        help_text="Custom metadata"
    )

    class Meta:
        db_table = "core_schedule_holidays"
        ordering = ["start_datetime"]

    def __str__(self):
        return self.name
