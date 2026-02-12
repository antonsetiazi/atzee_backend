# core/schedule/recurring/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Recurring(TenantAwareModel):
    """
    Recurring rule for events.
    Example:
        - Daily meeting
        - Weekly class
        - Monthly billing cycle
    """

    FREQUENCY_CHOICES = [
        ("daily", "Daily"),
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    ]

    event = models.ForeignKey(
        "core_schedule_events.Event",
        on_delete=models.CASCADE,
        related_name="recurrings"
    )

    frequency = models.CharField(
        max_length=20,
        choices=FREQUENCY_CHOICES
    )

    interval = models.PositiveIntegerField(
        default=1,
        help_text="Repeat every X frequency units"
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="Optional end date for recurrence"
    )

    class Meta:
        db_table = "core_schedule_recurrings"
        ordering = ["frequency"]

    def __str__(self):
        return f"{self.event.title} - {self.frequency}"
