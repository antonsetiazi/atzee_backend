# core/master/locations/apps.py

from django.apps import AppConfig


class LocationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.master.locations"
    label = "core_master_locations"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.location_list import LocationListEntity
        from .entities.location_select_list import LocationSelectListEntity

        register_entity(LocationListEntity())
        register_entity(LocationSelectListEntity())
