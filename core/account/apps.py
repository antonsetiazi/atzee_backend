# core/account/apps.py

from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.account"
    label = "core_account"

    def ready(self):
        from core.entities.registry import register_entity
        from core.account.entities.profile import AccountProfileEntity
        from core.account.entities.profile_update import AccountProfileUpdateEntity

        register_entity(AccountProfileEntity())
        register_entity(AccountProfileUpdateEntity())
