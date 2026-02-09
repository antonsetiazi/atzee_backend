# core/geo/countries/apps.py

from django.apps import AppConfig


class CountriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.geo.countries"
    label = "core_geo_countries"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.country_list import CountryListEntity
        from .entities.country_select_list import CountrySelectListEntity

        register_entity(CountryListEntity())
        register_entity(CountrySelectListEntity())
