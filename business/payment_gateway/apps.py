# business/payment_gateway/apps.py

from django.apps import AppConfig


class PaymentGatewayConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.payment_gateway"
    label = "business_payment_gateway"
