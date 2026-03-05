# verticals/cbs/apps.py

from django.apps import AppConfig

class CbsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.cbs"
    label = "verticals_cbs"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.cbs.seeds.permissions

        # from core.entities.registry import register_entity
        # from verticals.cbs.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.cbs.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())