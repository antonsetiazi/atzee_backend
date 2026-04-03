# business/payment_gateway/selectors.py

from business.payment_gateway.models import PaymentMethod, PaymentGatewayConfig


def get_payment_methods(*, tenant):
    return PaymentMethod.objects.filter(
        tenant=tenant,
        is_deleted=False
    ).order_by("order", "id")


def get_gateway_configs(*, tenant):
    return PaymentGatewayConfig.objects.filter(
        tenant=tenant,
        is_deleted=False
    )