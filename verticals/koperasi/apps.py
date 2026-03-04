# verticals/koperasi/apps.py

from django.apps import AppConfig

class KoperasiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.koperasi"
    label = "verticals_koperasi"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.koperasi.seeds.permissions

        # from core.entities.registry import register_entity
        # from verticals.koperasi.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.koperasi.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())