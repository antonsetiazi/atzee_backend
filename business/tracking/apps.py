# business/tracking/apps.py

from django.apps import AppConfig


class TrackingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.tracking"
    label = "business_tracking"

