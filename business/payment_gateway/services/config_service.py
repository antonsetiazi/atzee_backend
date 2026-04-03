# business/payment_gateway/services/config_service.py

from django.db import transaction
from django.core.exceptions import ValidationError

from business.payment_gateway.models import PaymentGatewayConfig


@transaction.atomic
def upsert_gateway_config(
    *,
    tenant,
    provider,
    environment,
    is_active,
    api_key,
    secret_key=None,
    merchant_id=None,
    extra_config=None,
):
    config, _ = PaymentGatewayConfig.objects.update_or_create(
        tenant=tenant,
        provider=provider,
        defaults={
            "environment": environment,
            "is_active": is_active,
            "api_key": api_key,
            "secret_key": secret_key,
            "merchant_id": merchant_id,
            "extra_config": extra_config,
        }
    )

    return config