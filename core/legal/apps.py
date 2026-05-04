# core/legal/apps.py

from django.apps import AppConfig


class LegalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.legal"
    label = "core_legal"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity

        from .entities.policy_list import PolicyListEntity
        from .entities.policy_create import PolicyCreateEntity
        from .entities.policy_detail import PolicyDetailEntity
        from .entities.policy_update import PolicyUpdateEntity
        from .entities.policy_delete import PolicyDeleteEntity

        register_entity(PolicyListEntity())
        register_entity(PolicyCreateEntity())
        register_entity(PolicyDetailEntity())
        register_entity(PolicyUpdateEntity())
        register_entity(PolicyDeleteEntity())