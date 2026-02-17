# core/account/models.py

from django.db import models
from django.conf import settings


class UserSettings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="settings",
    )

    # UI Preferences
    theme = models.CharField(
        max_length=20,
        default="light",
    )

    language = models.CharField(
        max_length=10,
        default="en",
    )

    timezone = models.CharField(
        max_length=50,
        default="UTC",
    )

    # Notifications
    email_notifications = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_user_settings"

    def __str__(self):
        return f"Settings for {self.user.username}"
