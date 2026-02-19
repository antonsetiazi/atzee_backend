from django.apps import AppConfig


class UIConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.ui"
    label = "core_ui"

    def ready(self):
        from . import bootstrap