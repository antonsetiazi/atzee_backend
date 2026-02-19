# core/classifications/labels/apps.py

from django.apps import AppConfig


class LabelsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.classifications.labels"
    label = "core_classifications_labels"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.label_list import LabelListEntity
        from .entities.label_select_list import LabelSelectListEntity

        register_entity(LabelListEntity())
        register_entity(LabelSelectListEntity())
