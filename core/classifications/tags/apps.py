# core/classifications/tags/apps.py

from django.apps import AppConfig


class TagsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.classifications.tags"
    label = "core_classifications_tags"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.tag_list import TagListEntity
        from .entities.tag_select_list import TagSelectListEntity

        register_entity(TagListEntity())
        register_entity(TagSelectListEntity())
