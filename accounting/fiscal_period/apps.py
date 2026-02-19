from django.apps import AppConfig


class FiscalPeriodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounting.fiscal_period"
    label = "accounting_fiscal_period"


    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from accounting.fiscal_period.entities.fiscal_period_list import FiscalPeriodListEntity

        register_entity(FiscalPeriodListEntity())