# verticals/isp/apps.py

from django.apps import AppConfig

class IspConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.isp"
    label = "verticals_isp"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.isp.seeds.permissions

        # from core.entities.registry import register_entity
        # from verticals.isp.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.isp.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())