# marketplace/services/order_start_service.py

from django.db import transaction
from django.core.exceptions import ValidationError

from marketplace.models.order import Order, OrderStatus, PaymentStatus
from business.booking.models import Booking
from business.booking.services.start import start_booking

from core.notifications.services import NotificationService
from core.notifications.events import SESSION_STARTED


@transaction.atomic
def start_order(*, tenant, order_id, partner):
    order = (
        Order.objects
        .select_for_update()
        .filter(tenant=tenant, id=order_id)
        .first()
    )

    if not order:
        raise ValidationError("Order tidak ditemukan")

    # 🔒 VALIDATION
    if order.partner != partner:
        raise ValidationError("Bukan partner dari order ini")

    if order.payment_status != PaymentStatus.PAID:
        raise ValidationError("Order belum dibayar")

    if order.status != OrderStatus.ACCEPTED:
        raise ValidationError("Order belum bisa dimulai")

    # 🔥 UPDATE STATUS
    order.status = OrderStatus.ON_GOING
    order.save(update_fields=["status", "updated_at"])

    # ==================================================
    # 🔔 NOTIFY CUSTOMER
    # ==================================================
    NotificationService.notify(
        user=order.user,
        tenant=tenant,
        event=SESSION_STARTED,
        title="Pesanan Dimulai",
        message="Partner telah mulai mengerjakan pesanan Anda.",
        entity_type="order",
        entity_id=str(order.id),
    )

    # 🔗 START BOOKING (optional, kalau ada)
    if order.booking_id:
        try:
            booking = Booking.objects.get(id=order.booking_id)
            start_booking(booking)
        except Booking.DoesNotExist:
            pass

    return order