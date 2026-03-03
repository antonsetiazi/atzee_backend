# verticals/pesantren/apps.py

from django.apps import AppConfig

class PesantrenConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.pesantren"
    label = "verticals_pesantren"

    # def ready(self):
        # from .ui import bootstrap 
        # import verticals.pesantren.seeds.permissions

        # from core.entities.registry import register_entity
        # from verticals.pesantren.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.pesantren.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())