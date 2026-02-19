# core/org/departments/apps.py

from django.apps import AppConfig


class DepartmentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.org.departments"
    label = "core_org_departments"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.department_list import DepartmentListEntity
        from .entities.department_select_list import DepartmentSelectListEntity

        register_entity(DepartmentListEntity())
        register_entity(DepartmentSelectListEntity())
