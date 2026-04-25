# core/realtime/apps.py

from django.apps import AppConfig


class RealtimeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.realtime"
    label = "core_realtime"
