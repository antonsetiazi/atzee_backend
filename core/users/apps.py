from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.users"
    label = "core_users"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.user_list import UserListEntity

        register_entity(UserListEntity())