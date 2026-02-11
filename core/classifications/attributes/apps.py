# core/classifications/attributes/apps.py

from django.apps import AppConfig


class AttributesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.classifications.attributes"
    label = "core_classifications_attributes"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.attribute_list import AttributeListEntity
        from .entities.attribute_select_list import AttributeSelectListEntity
        from .entities.attribute_option_list import AttributeOptionListEntity

        register_entity(AttributeListEntity())
        register_entity(AttributeSelectListEntity())
        register_entity(AttributeOptionListEntity())
