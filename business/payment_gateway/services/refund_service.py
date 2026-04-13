# business/payment_gateway/services/refund_service.py

import requests
import base64

from django.core.exceptions import ValidationError

from business.payment_gateway.models import PaymentGateway, PaymentGatewayConfig


def _get_midtrans_headers(server_key: str):
    encoded = base64.b64encode(f"{server_key}:".encode()).decode()

    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Basic {encoded}",
    }


def refund_midtrans_payment(*, payment: PaymentGateway, amount=None, reason="Refund"):
    """
    Call Midtrans refund API
    """

    if payment.provider != PaymentGateway.PROVIDER_MIDTRANS:
        raise ValidationError("Refund only supports Midtrans for now")

    if payment.status != PaymentGateway.STATUS_SUCCESS:
        raise ValidationError("Payment not in SUCCESS state")

    config = PaymentGatewayConfig.objects.filter(
        tenant=payment.tenant,
        provider=PaymentGateway.PROVIDER_MIDTRANS,
        is_active=True
    ).first()

    if not config:
        raise ValidationError("Midtrans config not found")

    base_url = (
        "https://api.midtrans.com"
        if config.environment == "production"
        else "https://api.sandbox.midtrans.com"
    )

    url = f"{base_url}/v2/{payment.external_reference}/refund"

    headers = _get_midtrans_headers(config.api_key)

    payload = {
        "refund_key": f"refund-{payment.id}",
        "amount": int(float(amount or payment.amount)),
        "reason": reason,
    }

    response = requests.post(url, json=payload, headers=headers)

    try:
        data = response.json()
    except Exception:
        raise Exception(f"Midtrans refund invalid response: {response.text}")

    if response.status_code not in [200, 201]:
        raise Exception(f"Midtrans refund failed: {data}")

    return data