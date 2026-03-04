# verticals/hrms/apps.py

from django.apps import AppConfig

class HRMSConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.hrms"
    label = "verticals_hrms"

    def ready(self):
        from .ui import bootstrap 
        # import verticals.hrms.seeds.permissions

        from core.entities.registry import register_entity
        # from verticals.hrms.entities.cashier_dashboard import CashierDashboardEntity
        # from verticals.hrms.entities.cashier_sales import CashierSalesEntity

        # register_entity(CashierDashboardEntity())
        # register_entity(CashierSalesEntity())