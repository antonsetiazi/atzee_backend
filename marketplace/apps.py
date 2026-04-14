# marketplace/apps.py

from django.apps import AppConfig


class MarketplaceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "marketplace"
    label = "marketplace"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.order_list import OrderListEntity

        register_entity(OrderListEntity())