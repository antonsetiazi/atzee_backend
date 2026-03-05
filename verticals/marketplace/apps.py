# verticals/marketplace/apps.py

from django.apps import AppConfig

class MarketplaceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.marketplace"
    label = "verticals_marketplace"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.marketplace.seeds.permissions

        # from core.entities.registry import register_entity
        # from verticals.marketplace.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.marketplace.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())