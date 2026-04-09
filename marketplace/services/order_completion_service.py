# marketplace/services/order_completion_service.py

from django.db import transaction
from django.utils import timezone

from marketplace.models.order import Order, OrderStatus, PaymentStatus
from business.booking.services.complete_by_id import complete_booking_by_id


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

    # =========================
    # 🔗 BOOKING COMPLETION
    # =========================
    if order.booking_id:
        try:
            complete_booking_by_id(order.booking_id)
        except ValueError:
            pass

    # =========================
    # 💾 UPDATE ORDER
    # =========================
    order.status = OrderStatus.COMPLETED
    order.completed_at = timezone.now()
    order.save(update_fields=["status", "completed_at"])

    # =========================
    # 🔥 FUTURE: FINANCIAL TRIGGER
    # =========================
    # TODO:
    # - revenue split
    # - wallet update
    # - accounting journal

    return order