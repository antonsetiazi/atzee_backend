# business/users/apps.py

from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.users"
    label = "business_users"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.user_list import UserListEntity
        from .entities.profile import BusinessUserProfileEntity
        from .entities.profile_update import BusinessUserProfileUpdateEntity

        register_entity(UserListEntity())
        register_entity(BusinessUserProfileEntity())
        register_entity(BusinessUserProfileUpdateEntity())
