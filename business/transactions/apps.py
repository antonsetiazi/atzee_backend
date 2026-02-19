from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.transactions"
    label = "business_transactions"


    def ready(self):
        from business.sales.ui import bootstrap
        from core.entities.registry import register_entity
        from business.sales.entities.sales_direct_list import SalesDirectListEntity
        from business.sales.entities.sales_direct_items import SalesDirectItemsEntity

        register_entity(SalesDirectListEntity())
        register_entity(SalesDirectItemsEntity())