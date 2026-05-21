# verticals/hr/apps.py

from django.apps import AppConfig


class HrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.hr"
    label = "verticals_hr"

    def ready(self):
        from core.entities.registry import register_entity
        from verticals.hr.entities.admin_dashboard import AdminDashboardEntity
        from verticals.hr.entities.guest_home import GuestHomeEntity

        from .ui import bootstrap

        register_entity(GuestHomeEntity())
        register_entity(AdminDashboardEntity())
