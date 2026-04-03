# marketplace/services/payment_service.py

from django.db import transaction
from django.utils import timezone

from marketplace.models import Order
from business.booking.models import Booking
from business.booking.services.confirm import confirm_booking


@transaction.atomic
def handle_order_payment_by_id(order_id: str, payment):
    """
    Handle payment success for order domain
    """

    order = (
        Order.objects
        .select_for_update()
        .filter(id=order_id)
        .first()
    )

    if not order:
        return

    # 🔁 IDEMPOTENCY
    if order.status == "paid":
        return

    # =========================
    # 🔗 BOOKING LOGIC
    # =========================
    if order.booking_id:
        try:
            booking = Booking.objects.select_for_update().get(id=order.booking_id)
            confirm_booking(booking)
        except Booking.DoesNotExist:
            pass

    # =========================
    # 💾 UPDATE ORDER
    # =========================
    order.status = "paid"
    order.paid_at = timezone.now()
    order.save(update_fields=["status", "paid_at"])