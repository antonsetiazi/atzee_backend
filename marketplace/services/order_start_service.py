# marketplace/services/order_start_service.py

from django.db import transaction
from django.core.exceptions import ValidationError

from marketplace.models.order import Order, OrderStatus, PaymentStatus
from business.booking.models import Booking
from business.booking.services.start import start_booking

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

    # 🔗 START BOOKING (optional, kalau ada)
    if order.booking_id:
        try:
            booking = Booking.objects.get(id=order.booking_id)
            start_booking(booking)
        except Booking.DoesNotExist:
            pass

    return order