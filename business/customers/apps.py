# business/customers/apps.py

from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.customers"
    label = "business_customers"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.customer_list import CustomerListEntity
        from .entities.customer_create import CustomerCreateEntity

        register_entity(CustomerListEntity())
        register_entity(CustomerCreateEntity())
