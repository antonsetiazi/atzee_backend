# core/schedule/reminders/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Reminder(TenantAwareModel):
    """
    Reminder / notification for events
    """

    REMINDER_TYPE_CHOICES = [
        ("email", "Email"),
        ("in_app", "In-App"),
        ("wa", "WhatsApp"),
    ]

    event = models.ForeignKey(
        "core_schedule_events.Event",
        on_delete=models.CASCADE,
        related_name="reminders"
    )

    reminder_time = models.DurationField(
        help_text="Time before event to trigger reminder"
    )

    reminder_type = models.CharField(
        max_length=20,
        choices=REMINDER_TYPE_CHOICES,
        default="in_app"
    )

    repeat_interval = models.DurationField(
        blank=True,
        null=True,
        help_text="Optional repeat interval for reminder"
    )

    class Meta:
        db_table = "core_schedule_reminders"
        ordering = ["reminder_time"]

    def __str__(self):
        return f"{self.event.title} - {self.reminder_type}"

