# marketplace/services/order_completion_service.py

from decimal import Decimal

from django.db import transaction
from django.utils import timezone

from marketplace.models.order import Order, OrderStatus, PaymentStatus
from business.booking.services.complete_by_id import complete_booking_by_id

from core.wallet import services as wallet_services
from core.wallet import selectors as wallet_selectors


@transaction.atomic
def complete_order(order_id: int, user):
    order = (
        Order.objects
        .select_for_update()
        .filter(id=order_id)
        .first()
    )

    if not order:
        raise ValueError("Order tidak ditemukan")

    # 🔒 VALIDATION
    if order.user_id != user.id:
        raise PermissionError("Bukan pemilik order")

    # payment must be paid
    if order.payment_status != PaymentStatus.PAID:
        raise ValueError("Order belum dibayar")
    
    # only accepted / on_going can complete
    if order.status not in [
        OrderStatus.ACCEPTED,
        OrderStatus.ON_GOING,
    ]:
        raise ValueError("Order belum dapat diselesaikan")

    if not order.partner:
        raise ValueError("Partner belum ditentukan")
    
    if not order.partner.core_user:
        raise ValueError("Partner belum terhubung ke user")

    # =========================
    # 🔗 BOOKING COMPLETION
    # =========================
    if order.booking_id:
        try:
            complete_booking_by_id(order.booking_id)
        except ValueError:
            pass


    # =========================================================
    # 💰 ESCROW RELEASE → PARTNER WALLET
    # =========================================================
  
    user_wallet = wallet_selectors.get_wallet_or_create(
        tenant=order.tenant,
        user=order.user
    )

    # system_wallet = wallet_selectors.get_system_wallet(
    #     tenant=order.tenant
    # )
    
    partner_wallet = wallet_selectors.get_wallet_or_create(
        tenant=order.tenant,
        user=order.partner.core_user
    )
    
    amount = Decimal(order.total_amount)

    wallet_services.escrow_release_to_partner(
        tenant=order.tenant,
        user_wallet=user_wallet,
        partner_wallet=partner_wallet,
        amount=amount,
        reference_type="order",
        reference_id=str(order.id),
        idempotency_key=f"release-order-{order.id}",
        description="Order completed - release to partner"
    )


    # =========================
    # 💾 UPDATE ORDER
    # =========================
    order.status = OrderStatus.COMPLETED
    order.completed_at = timezone.now()
    order.save(update_fields=["status", "completed_at", "updated_at"])

    return order