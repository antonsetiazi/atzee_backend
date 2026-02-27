# core/notifications/apps.py

from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.notifications"
    label = "core_notifications"

    def ready(self):
        from .ui import bootstrap