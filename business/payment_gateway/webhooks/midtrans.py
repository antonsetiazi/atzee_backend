# business/payment_gateway/webhooks/midtrans.py

import logging

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import transaction

from business.payment_gateway.models import (
    PaymentGateway,
    PaymentGatewayConfig,
)
from business.payment_gateway.providers.midtrans import MidtransProvider
from business.payment_gateway.services.gateway_service import (
    handle_payment_success,
    handle_payment_failed,
    handle_payment_expired,
)

logger = logging.getLogger(__name__)


@api_view(["POST"])
@permission_classes([AllowAny])
@transaction.atomic
def midtrans_webhook(request):
    try:
        payload = request.data
        logger.info("🔥 Midtrans webhook received", extra={"payload": payload})

        # =========================================================
        # 1. Ambil order_id DULU (tanpa validasi)
        # =========================================================
        external_reference = payload.get("order_id")

        if not external_reference:
            logger.warning("⚠️ Missing order_id", extra={"payload": payload})
            return Response({"status": "missing order_id"}, status=200)

        # =========================================================
        # 2. Ambil payment + lock (anti race condition)
        # =========================================================
        payment = (
            PaymentGateway.objects
            .select_related("tenant")
            .select_for_update()
            .filter(external_reference=external_reference)
            .first()
        )

        if not payment:
            logger.warning(
                "⚠️ Payment not found",
                extra={"external_reference": external_reference}
            )
            return Response({"status": "not found"}, status=200)

        # =========================================================
        # 3. Ambil config berdasarkan tenant + provider
        # =========================================================
        config = (
            PaymentGatewayConfig.objects
            .filter(
                tenant=payment.tenant,
                provider="midtrans",
                is_active=True,
            )
            .first()
        )

        if not config:
            logger.error(
                "❌ Midtrans config not found",
                extra={
                    "tenant_id": str(payment.tenant_id),
                    "external_reference": external_reference,
                },
            )
            return Response({"status": "config missing"}, status=200)

        provider = MidtransProvider(config=config)

        # =========================================================
        # 4. VALIDATE SIGNATURE (SETELAH ADA CONFIG)
        # =========================================================
        if not provider.validate_signature(payload):
            logger.warning(
                "❌ Invalid Midtrans signature",
                extra={"external_reference": external_reference},
            )
            return Response({"status": "invalid signature"}, status=200)

        # =========================================================
        # 5. Parse webhook
        # =========================================================
        data = provider.parse_webhook(payload)

        status = data.get("status")

        if not status:
            logger.warning(
                "⚠️ Missing status after parsing",
                extra={"external_reference": external_reference},
            )
            return Response({"status": "invalid payload"}, status=200)

        # =========================================================
        # 6. Idempotency (ANTI DOUBLE UPDATE)
        # =========================================================
        if payment.status == status:
            logger.info(
                "🔁 Duplicate webhook ignored",
                extra={
                    "external_reference": external_reference,
                    "status": status,
                },
            )
            return Response({"status": "duplicate ignored"}, status=200)

        # =========================================================
        # 7. Simpan audit trail
        # =========================================================
        payment.raw_webhook = payload
        payment.external_id = data.get("external_id")
        payment.save(update_fields=["raw_webhook", "external_id"])

        # =========================================================
        # 8. Trigger domain logic
        # =========================================================
        if status == PaymentGateway.STATUS_SUCCESS:
            handle_payment_success(payment=payment, payload=payload)

        elif status == PaymentGateway.STATUS_FAILED:
            handle_payment_failed(payment=payment, payload=payload)

        elif status == PaymentGateway.STATUS_EXPIRED:
            handle_payment_expired(payment=payment, payload=payload)

        else:
            logger.info(
                "ℹ️ Unhandled status",
                extra={
                    "status": status,
                    "external_reference": external_reference,
                },
            )

        return Response({"status": "ok"}, status=200)

    except Exception:
        logger.exception("💥 Midtrans webhook error")

        # ❗ WAJIB 200 supaya Midtrans tidak retry spam
        return Response({"status": "error handled"}, status=200)