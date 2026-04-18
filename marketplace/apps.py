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
        from .entities.partner_product_list import PartnerProductListEntity
        from .entities.partner_product_detail import PartnerProductDetailEntity
        from .entities.partner_product_update import PartnerProductUpdateEntity
        from .entities.partner_product_create import PartnerProductCreateEntity

        register_entity(OrderListEntity())
        register_entity(PartnerProductListEntity())
        register_entity(PartnerProductDetailEntity())
        register_entity(PartnerProductUpdateEntity())
        register_entity(PartnerProductCreateEntity())