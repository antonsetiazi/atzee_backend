# verticals/ustadzku/apps.py

from django.apps import AppConfig

class UstadzkuConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.ustadzku"
    label = "verticals_ustadzku"

    def ready(self):
        from .dashboards.ui import bootstrap 
        import verticals.ustadzku.seeds.permissions

        from core.entities.registry import register_entity
        from verticals.ustadzku.entities.user_dashboard import UserDashboardEntity

        register_entity(UserDashboardEntity())