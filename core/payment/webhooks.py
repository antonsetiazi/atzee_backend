# core/payment/webhooks.py

import hashlib
import json

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.payment.models import Payment, PaymentStatus
from core.payment.services import can_transition


def _verify_midtrans_signature(payload: dict) -> bool:
    """
    Verify signature key from Midtrans
    """

    order_id = payload.get("order_id")
    status_code = payload.get("status_code")
    gross_amount = payload.get("gross_amount")
    signature_key = payload.get("signature_key")

    if not all([order_id, status_code, gross_amount, signature_key]):
        return False

    raw_string = (
        order_id +
        status_code +
        gross_amount +
        settings.MIDTRANS_SERVER_KEY
    )

    expected_signature = hashlib.sha512(raw_string.encode()).hexdigest()

    return expected_signature == signature_key


def _map_midtrans_status(transaction_status: str) -> str:
    if transaction_status in ["settlement", "capture"]:
        return PaymentStatus.SUCCESS

    if transaction_status in ["deny", "cancel", "expire"]:
        return PaymentStatus.FAILED

    if transaction_status in ["pending"]:
        return PaymentStatus.PENDING

    return PaymentStatus.FAILED


@csrf_exempt
def midtrans_webhook(request):

    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"detail": "Invalid JSON"}, status=400)

    # 🔐 Verify signature
    if not _verify_midtrans_signature(payload):
        return JsonResponse({"detail": "Invalid signature"}, status=403)

    order_id = payload.get("order_id")
    transaction_status = payload.get("transaction_status")

    if not order_id:
        return JsonResponse({"detail": "Missing order_id"}, status=400)

    try:
        payment = Payment.objects.get(external_id=order_id)
    except Payment.DoesNotExist:
        return JsonResponse({"detail": "Payment not found"}, status=404)

    # 🧠 Idempotency protection
    new_status = _map_midtrans_status(transaction_status)

    # 🧠 Idempotency + transition rule
    if can_transition(payment.status, new_status):
        payment.status = new_status
        payment.gateway_response = payload
        payment.save(update_fields=["status", "gateway_response", "updated_at"])

    return JsonResponse({"detail": "OK"})


def _verify_xendit_token(request) -> bool:
    callback_token = request.headers.get("X-Callback-Token")
    return callback_token == settings.XENDIT_CALLBACK_TOKEN


def _map_xendit_status(status: str) -> str:
    if status in ["PAID", "SETTLED"]:
        return PaymentStatus.SUCCESS

    if status in ["FAILED", "EXPIRED", "VOIDED"]:
        return PaymentStatus.FAILED

    if status in ["PENDING"]:
        return PaymentStatus.PENDING

    return PaymentStatus.FAILED


@csrf_exempt
def xendit_webhook(request):

    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    # 🔐 Verify token
    if not _verify_xendit_token(request):
        return JsonResponse({"detail": "Invalid callback token"}, status=403)

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"detail": "Invalid JSON"}, status=400)

    external_id = payload.get("external_id")
    status_value = payload.get("status")

    if not external_id:
        return JsonResponse({"detail": "Missing external_id"}, status=400)

    try:
        payment = Payment.objects.get(external_id=external_id)
    except Payment.DoesNotExist:
        return JsonResponse({"detail": "Payment not found"}, status=404)

    new_status = _map_xendit_status(status_value)

    # 🧠 Idempotency protection
    if can_transition(payment.status, new_status):
        payment.status = new_status
        payment.gateway_response = payload
        payment.save(update_fields=["status", "gateway_response", "updated_at"])

    return JsonResponse({"detail": "OK"})