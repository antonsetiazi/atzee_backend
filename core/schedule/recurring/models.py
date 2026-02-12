# core/schedule/recurring/models.py

from django.db import models
from core.models.base import TenantAwareModel


class RecurringRule(TenantAwareModel):
    """
    Recurring rule for events
    """

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="recurring_rules"
    )

    rrule = models.TextField(
        help_text="iCal RRULE string for recurring events"
    )

    end_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Optional end date for recurring"
    )

    exceptions = models.JSONField(
        blank=True,
        null=True,
        help_text="List of dates to skip"
    )

    class Meta:
        db_table = "core_schedule_recurring"
