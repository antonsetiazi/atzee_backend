# core/geo/villages/apps.py

from django.apps import AppConfig


class VillagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.geo.villages"
    label = "core_geo_villages"

