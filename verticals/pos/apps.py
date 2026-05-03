# verticals/pos/apps.py

from django.apps import AppConfig

class PosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.pos"
    label = "verticals_pos"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.pos.seeds.permissions

        from core.entities.registry import register_entity
        from verticals.pos.entities.cashier_dashboard import CashierDashboardEntity
        from verticals.pos.entities.cashier_sales import CashierSalesEntity

        register_entity(CashierDashboardEntity())
        register_entity(CashierSalesEntity())