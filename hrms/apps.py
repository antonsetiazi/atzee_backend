# hrms/apps.py

from django.apps import AppConfig


class HrmsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "hrms"
    label = "hrms"

    # def ready(self):
    # from .ui import bootstrap

    # from core.entities.registry import register_entity
