# verticals/finance/apps.py

from django.apps import AppConfig

class FinanceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.finance"
    label = "verticals_finance"

    def ready(self):
        from .ui import bootstrap

        from core.entities.registry import register_entity
        from verticals.finance.entities.guest_home import GuestHomeEntity
        from verticals.finance.entities.admin_dashboard import AdminDashboardEntity

        register_entity(GuestHomeEntity())
        register_entity(AdminDashboardEntity())