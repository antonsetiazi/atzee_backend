# verticals/distributor/apps.py

from django.apps import AppConfig

class DistributorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.distributor"
    label = "verticals_distributor"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.distributor.seeds.permissions

        from core.entities.registry import register_entity
        # from verticals.distributor.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.distributor.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())