# verticals/research/apps.py

from django.apps import AppConfig

class ResearchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.research"
    label = "verticals_research"

    def ready(self):
        from .ui import bootstrap  
        # import verticals.research.seeds.permissions

        from core.entities.registry import register_entity
        # from verticals.research.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.research.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())