# verticals/bengkel/apps.py

from django.apps import AppConfig

class BengkelConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.bengkel"
    label = "verticals_bengkel"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.bengkel.seeds.permissions

        from core.entities.registry import register_entity
        # from verticals.bengkel.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.bengkel.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())