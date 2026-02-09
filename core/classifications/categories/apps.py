# core/classifications/categories/apps.py

from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.classifications.categories"
    label = "core_classifications_categories"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.category_list import CategoryListEntity
        from .entities.category_select_list import CategorySelectListEntity

        register_entity(CategoryListEntity())
        register_entity(CategorySelectListEntity())
