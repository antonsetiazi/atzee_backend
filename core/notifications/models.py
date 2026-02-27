# core/notifications/models.py

from django.db import models
from core.users.models import User
from core.tenants.models import Tenant

from core.notifications.events import ALL_NOTIFICATION_EVENTS

class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications"
    )

    # Business event type
    event = models.CharField(
        max_length=100,
        choices=[(e, e) for e in ALL_NOTIFICATION_EVENTS],
        help_text="booking_accepted, payment_success, session_started, etc"
    )

    # UI severity
    level = models.CharField(
        max_length=20,
        default="info",
        help_text="info | warning | error"
    )

    title = models.CharField(max_length=255)
    message = models.TextField()

    # Domain linking
    entity_type = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    entity_id = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    payload = models.JSONField(
        null=True,
        blank=True,
        help_text="Optional structured data for frontend navigation"
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "core_notifications"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user", "is_read"]),
            models.Index(fields=["user", "created_at"]),
            models.Index(fields=["event"]),
        ]

    
    def __str__(self):
        return f"[{self.event}] {self.title}"