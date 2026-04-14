# business/payment_gateway/apps.py

from django.apps import AppConfig


class PaymentGatewayConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.payment_gateway"
    label = "business_payment_gateway"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.payment_gateway_list import PaymentGatewayListEntity

        register_entity(PaymentGatewayListEntity())