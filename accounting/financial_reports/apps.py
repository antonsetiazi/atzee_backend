from django.apps import AppConfig


class FinancialReportsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounting.financial_reports"
    label = "accounting_financial_reports"

    def ready(self):
        from .ui import bootstrap