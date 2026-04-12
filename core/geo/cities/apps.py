# core/geo/cities/apps.py

from django.apps import AppConfig


class CitiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.geo.cities"
    label = "core_geo_cities"

