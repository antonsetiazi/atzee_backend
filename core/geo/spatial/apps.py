# core/geo/spatial/apps.py

from django.apps import AppConfig


class SpatialConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.geo.spatial"
    label = "core_geo_spatial"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.location_attach import LocationAttachEntity
        from .entities.location_list import LocationListEntity
        from .entities.location_update import LocationUpdateEntity
        from .entities.location_delete import LocationDeleteEntity

        register_entity(LocationAttachEntity())
        register_entity(LocationListEntity())
        register_entity(LocationUpdateEntity())
        register_entity(LocationDeleteEntity())
