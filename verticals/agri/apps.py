# verticals/agri/apps.py

from django.apps import AppConfig 

class AgriConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.agri"
    label = "verticals_agri"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.agri.seeds.permissions

        from core.entities.registry import register_entity
        # from verticals.agri.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.agri.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())