# marketplace/services/payment_service.py

from decimal import Decimal

from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError

from marketplace.models import Order
from marketplace.models.order import PaymentStatus

from business.booking.models import Booking
from business.booking.services.confirm import confirm_booking

from core.wallet import services as wallet_services
from core.wallet import selectors as wallet_selectors


@transaction.atomic
def handle_order_payment_by_id(order_id: str, payment=None, tenant=None):
    """
    Handle payment success for order domain (ESCROW ENABLED)
    """
    if payment:
        tenant = payment.tenant

    if not tenant:
        raise ValidationError("Tenant required")
    
    order = (
        Order.objects
        .select_for_update()
        .filter(id=order_id, tenant=tenant)
        .first()
    )

    if not order:
        raise ValidationError("Order not found")

    # =========================================================
    # 🔁 IDEMPOTENCY (SUPER IMPORTANT)
    # =========================================================
    if order.payment_status == PaymentStatus.PAID:
        return order

    amount = Decimal(order.total_amount)

    # =========================================================
    # 💰 SYSTEM WALLET (ESCROW POOL)
    # =========================================================
    system_wallet = wallet_selectors.get_system_wallet(
        tenant=order.tenant
    )

    # =========================================================
    # 💰 USER WALLET (SOURCE OF TRUTH FOR MVP)
    # =========================================================
    user_wallet = wallet_selectors.get_wallet_or_create(
        tenant=order.tenant,
        user=order.user
    )

    if payment:
        # =========================================================
        # 💰 STEP 1: TOPUP (EXTERNAL → USER)
        # =========================================================
        wallet_services.topup_wallet(
            tenant=order.tenant,
            wallet=user_wallet,
            amount=amount,
            idempotency_key=f"topup-order-{order.id}",
            description="Payment received from Midtrans"
        )

        # =========================================================
        # 💰 STEP 2: ESCROW HOLD (USER AVAILABLE → HELD)
        # =========================================================
        wallet_services.escrow_hold(
            tenant=order.tenant,
            wallet=user_wallet,
            amount=amount,
            reference_type="order",
            reference_id=str(order.id),
            idempotency_key=f"escrow-hold-order-{order.id}",
            description="Escrow hold for order"
        )

    # =========================
    # 🔗 BOOKING LOGIC
    # =========================
    if order.booking_id:
        try:
            booking = Booking.objects.select_for_update().get(id=order.booking_id)
            confirm_booking(booking)
        except Booking.DoesNotExist:
            pass

    # =========================================================
    # 💾 UPDATE ORDER
    # =========================================================
    order.payment_status = PaymentStatus.PAID
    order.paid_at = timezone.now()

    order.save(update_fields=[
        "payment_status",
        "paid_at",
        "updated_at"
    ])

    return order