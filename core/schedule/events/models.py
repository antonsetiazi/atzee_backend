# core/schedule/events/models.py

from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel


class Event(TenantAwareModel, ExtensibleModel):
    """
    Core Event model (generic, multi-tenant)
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    all_day = models.BooleanField(default=False)

    participants = models.JSONField(
        blank=True,
        null=True,
        help_text="List of user IDs or participant info"
    )

    metadata = models.JSONField(
        blank=True,
        null=True,
        help_text="Custom metadata for business modules"
    )

    color = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Optional color for UI rendering"
    )

    class Meta:
        db_table = "core_schedule_events"
        ordering = ["start_datetime"]

    def __str__(self):
        return self.title
