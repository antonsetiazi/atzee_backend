# accounting/chart_of_accounts/apps.py

from django.apps import AppConfig


class ChartOfAccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounting.chart_of_accounts"
    label = "accounting_chart_of_accounts"

    def ready(self):
        import accounting.chart_of_accounts.lookups
        from core.entities.registry import register_entity
        from .entities.chart_of_account_list import ChartOfAccountListEntity
        from .entities.chart_of_account_create import ChartOfAccountCreateEntity

        register_entity(ChartOfAccountListEntity())
        register_entity(ChartOfAccountCreateEntity())