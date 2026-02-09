# core/org/branches/apps.py

from django.apps import AppConfig


class BranchesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.org.branches"
    label = "core_org_branches"


    def ready(self):
        from core.entities.registry import register_entity
        from .entities.branch_list import BranchListEntity
        from .entities.branch_select_list import BranchSelectListEntity

        register_entity(BranchListEntity())
        register_entity(BranchSelectListEntity())
