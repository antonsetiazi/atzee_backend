# business/payment_gateway/services/gateway_service.py

import logging

from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError

from business.payment_gateway.models import PaymentGateway, PaymentGatewayConfig
from business.payment_gateway.providers.base import BasePaymentProvider
from business.payment_gateway.providers.midtrans import MidtransProvider
from business.payment_gateway.providers.xendit import XenditProvider

logger = logging.getLogger(__name__)


# --------------------------------------------------
# 🔌 PROVIDER FACTORY
# --------------------------------------------------

def _get_provider(provider: str, config: PaymentGatewayConfig) -> BasePaymentProvider:
    if provider == PaymentGateway.PROVIDER_MIDTRANS:
        return MidtransProvider(config)
    elif provider == PaymentGateway.PROVIDER_XENDIT:
        return XenditProvider(config)
    else:
        raise ValidationError(f"Unsupported provider: {provider}")


# --------------------------------------------------
# 💰 CREATE PAYMENT
# --------------------------------------------------

@transaction.atomic
def create_payment(
    *,
    tenant,
    reference_type: str,
    reference_id: str,
    amount,
    provider: str,
    channel: str | None = None,
) -> PaymentGateway:
    """
    Create payment + call external gateway
    """

    # 🔹 1. Ambil config aktif
    config = PaymentGatewayConfig.objects.filter(
        tenant=tenant,
        provider=provider,
        is_active=True
    ).first()

    if not config:
        raise ValidationError("Payment gateway not configured.")

    # 🔹 2. Buat record local (PENDING)
    payment = PaymentGateway.objects.create(
        tenant=tenant,
        reference_type=reference_type,
        reference_id=reference_id,
        amount=amount,
        provider=provider,
        channel=channel,
        status=PaymentGateway.STATUS_PENDING,
    )

    # 🔹 3. Call provider
    provider_instance = _get_provider(provider, config)

    response = provider_instance.create_payment(payment)

    # 🔹 4. Save response
    payment.external_id = response.get("external_id")
    payment.external_reference = response.get("external_reference")
    payment.payment_url = response.get("payment_url")
    payment.payment_token = response.get("payment_token")
    payment.raw_response = response

    payment.save(update_fields=[
        "external_id",
        "external_reference",
        "payment_url",
        "payment_token",
        "raw_response",
        "updated_at"
    ])

    logger.info(
        "💳 Payment created",
        extra={
            "payment_id": payment.id,
            "external_reference": payment.external_reference,
        }
    )

    return payment


# --------------------------------------------------
# ✅ HANDLE SUCCESS
# --------------------------------------------------

@transaction.atomic
def handle_payment_success(
    *,
    payment: PaymentGateway,
    payload: dict | None = None
) -> PaymentGateway:
    """
    Mark payment as SUCCESS (idempotent + safe)
    """

    # 🔁 IDEMPOTENCY
    if payment.status == PaymentGateway.STATUS_SUCCESS:
        logger.info(
            "🔁 Payment already SUCCESS",
            extra={"payment_id": payment.id}
        )
        return payment

    # 🔒 Lock ulang (double safety)
    payment = PaymentGateway.objects.select_for_update().get(id=payment.id)

    # 🔁 Double check setelah lock
    if payment.status == PaymentGateway.STATUS_SUCCESS:
        return payment

    # 💾 Update payment
    payment.status = PaymentGateway.STATUS_SUCCESS
    payment.paid_at = timezone.now()
    payment.raw_webhook = payload or payment.raw_webhook

    payment.save(update_fields=[
        "status",
        "paid_at",
        "raw_webhook",
        "updated_at"
    ])

    logger.info(
        "✅ Payment SUCCESS",
        extra={"payment_id": payment.id}
    )

    # 🔗 Trigger domain logic (OUTSIDE payment concern)
    _on_payment_success(payment)

    return payment


# --------------------------------------------------
# ❌ HANDLE FAILED
# --------------------------------------------------

@transaction.atomic
def handle_payment_failed(
    *,
    payment: PaymentGateway,
    payload: dict | None = None
) -> PaymentGateway:

    if payment.status in [
        PaymentGateway.STATUS_SUCCESS,
        PaymentGateway.STATUS_FAILED
    ]:
        return payment

    payment = PaymentGateway.objects.select_for_update().get(id=payment.id)

    payment.status = PaymentGateway.STATUS_FAILED
    payment.raw_webhook = payload or payment.raw_webhook

    payment.save(update_fields=[
        "status",
        "raw_webhook",
        "updated_at"
    ])

    logger.warning(
        "❌ Payment FAILED",
        extra={"payment_id": payment.id}
    )

    return payment


# --------------------------------------------------
# ⏳ HANDLE EXPIRED
# --------------------------------------------------

@transaction.atomic
def handle_payment_expired(
    *,
    payment: PaymentGateway,
    payload: dict | None = None
) -> PaymentGateway:

    if payment.status != PaymentGateway.STATUS_PENDING:
        return payment

    payment = PaymentGateway.objects.select_for_update().get(id=payment.id)

    payment.status = PaymentGateway.STATUS_EXPIRED
    payment.raw_webhook = payload or payment.raw_webhook

    payment.save(update_fields=[
        "status",
        "raw_webhook",
        "updated_at"
    ])

    logger.info(
        "⏳ Payment EXPIRED",
        extra={"payment_id": payment.id}
    )

    return payment


# --------------------------------------------------
# 🔗 DOMAIN HOOK (VERY IMPORTANT)
# --------------------------------------------------

def _on_payment_success(payment: PaymentGateway):
    """
    Dispatch to domain service based on reference_type
    Payment layer TIDAK BOLEH tahu detail domain
    """

    try:
        # print("🔥 _on_payment_success CALLED", payment.id)

        if payment.reference_type == "order":
            # print("🔥 ORDER FLOW", payment.reference_id)

            # 👉 Import disini (lazy import)
            from marketplace.services.payment_service import handle_order_payment_by_id

            handle_order_payment_by_id(
                order_id=payment.reference_id,
                payment=payment
            )

        elif payment.reference_type == "wallet_topup":
            from core.wallet.payment_handlers import handle_wallet_topup

            handle_wallet_topup(payment)
        # future:
        # elif payment.reference_type == "invoice":
        # elif payment.reference_type == "subscription":

    except Exception:
        logger.exception("💥 Error in payment domain dispatch")