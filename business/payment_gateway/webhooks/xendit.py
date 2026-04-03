# business/payment_gateway/webhooks/xendit.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import transaction

from business.payment_gateway.models import PaymentGateway
from business.payment_gateway.providers.xendit import XenditProvider
from business.payment_gateway.services.gateway_service import (
    handle_payment_success,
    handle_payment_failed,
    handle_payment_expired,
)


@api_view(["POST"])
@permission_classes([AllowAny])
@transaction.atomic
def xendit_webhook(request):
    payload = request.data

    provider = XenditProvider(config=None)
    data = provider.parse_webhook(payload)

    external_reference = data.get("external_reference")

    payment = PaymentGateway.objects.filter(
        external_reference=external_reference
    ).first()

    if not payment:
        return Response({"detail": "Payment not found"}, status=404)

    status = data.get("status")

    if status == PaymentGateway.STATUS_SUCCESS:
        handle_payment_success(payment=payment, payload=payload)

    elif status == PaymentGateway.STATUS_FAILED:
        handle_payment_failed(payment=payment, payload=payload)

    elif status == PaymentGateway.STATUS_EXPIRED:
        handle_payment_expired(payment=payment, payload=payload)

    return Response({"status": "ok"})