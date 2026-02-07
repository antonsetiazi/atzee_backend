# core/master/uom/apps.py

from django.apps import AppConfig


class UOMConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.master.uom"
    label = "core_master_uom"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.uom_list import UOMListEntity

        register_entity(UOMListEntity())
