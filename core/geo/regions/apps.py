# core/geo/regions/apps.py

from django.apps import AppConfig


class RegionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.geo.regions"
    label = "core_geo_regions"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.region_list import RegionListEntity
        from .entities.region_select_list import RegionSelectListEntity

        register_entity(RegionListEntity())
        register_entity(RegionSelectListEntity())
