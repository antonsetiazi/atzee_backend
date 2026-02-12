# core/schedule/models/shift.py

from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel


class Shift(TenantAwareModel, ExtensibleModel):
    """
    Employee / participant shift schedule
    """

    name = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    participants = models.JSONField(
        blank=True,
        null=True,
        help_text="List of user IDs assigned to shift"
    )

    rotation_pattern = models.JSONField(
        blank=True,
        null=True,
        help_text="Optional rotation rules"
    )

    metadata = models.JSONField(
        blank=True,
        null=True,
        help_text="Custom metadata for business modules"
    )

    class Meta:
        db_table = "core_schedule_shifts"
        ordering = ["start_datetime"]

    def __str__(self):
        return self.name
