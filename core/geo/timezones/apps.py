# core/geo/timezones/apps.py

from django.apps import AppConfig


class TimezonesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.geo.timezones"
    label = "core_geo_timezones"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.timezone_list import TimezoneListEntity
        from .entities.timezone_select_list import TimezoneSelectListEntity

        register_entity(TimezoneListEntity())
        register_entity(TimezoneSelectListEntity())
