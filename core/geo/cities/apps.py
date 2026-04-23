# core/geo/cities/apps.py

from django.apps import AppConfig


class CitiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.geo.cities"
    label = "core_geo_cities"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.city_select_list import CitySelectListEntity

        register_entity(CitySelectListEntity())