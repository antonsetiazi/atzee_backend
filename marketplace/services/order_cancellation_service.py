# marketplace/services/order_cancellation_service.py

from decimal import Decimal

from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError

from marketplace.models.order import Order, OrderStatus, PaymentStatus

from business.booking.models import Booking, BookingStatus

from core.wallet import services as wallet_services
from core.wallet import selectors as wallet_selectors

from business.payment_gateway.models import PaymentGateway
from business.payment_gateway.services.refund_service import refund_midtrans_payment


@transaction.atomic
def cancel_order_by_partner(*, tenant, order_id, partner, reason: str = ""):
    """
    Partner cancel order AFTER PAYMENT → FULL REFUND
    """

    order = (
        Order.objects
        .select_for_update()
        .filter(tenant=tenant, id=order_id)
        .first()
    )

    if not order:
        raise ValidationError("Order tidak ditemukan")

    if order.selected_partner != partner:
        raise ValidationError("Tidak berhak cancel order ini")

    # 🔁 IDEMPOTENCY
    if order.status == OrderStatus.CANCELLED:
        return order

    # =========================================================
    # ❗ VALIDASI: hanya boleh cancel jika sudah bayar
    # =========================================================
    if order.payment_status != PaymentStatus.PAID:
        raise ValidationError("Order belum dibayar")

    amount = Decimal(order.total_amount)

    # =========================================================
    # 💰 ESCROW REFUND (INTERNAL)
    # =========================================================
    user_wallet = wallet_selectors.get_wallet_or_create(
        tenant=tenant,
        user=order.user
    )

    wallet_services.escrow_refund(
        tenant=tenant,
        wallet=user_wallet,
        amount=amount,
        reference_type="order",
        reference_id=str(order.id),
        idempotency_key=f"refund-order-{order.id}",
        description="Order cancelled by partner"
    )

    # =========================================================
    # 🌐 MIDTRANS REFUND (EXTERNAL)
    # =========================================================
    payment = PaymentGateway.objects.filter(
        tenant=tenant,
        reference_type="order",
        reference_id=str(order.id),
        status=PaymentGateway.STATUS_SUCCESS
    ).first()

    if payment:
        refund_midtrans_payment(
            payment=payment,
            amount=amount,
            reason="Order cancelled by partner"
        )

    # =========================================================
    # 🔗 BOOKING (PASSIVE EFFECT)
    # =========================================================
    if order.booking_id:
        Booking.objects.filter(id=order.booking_id).update(
            status=BookingStatus.CANCELED
        )

    # =========================================================
    # 💾 UPDATE ORDER
    # =========================================================
    order.status = OrderStatus.CANCELLED
    order.rejected_reason = reason
    order.rejected_at = timezone.now()
    order.save(update_fields=[
        "status",
        "rejected_reason",
        "rejected_at",
        "updated_at"
    ])

    return order