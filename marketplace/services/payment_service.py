# marketplace/services/payment_service.py

from business.booking.models import Booking
from business.booking.services.confirm import confirm_booking


def handle_payment_success(order):
    if order.booking_id:
        try:
            booking = Booking.objects.get(id=order.booking_id)
            confirm_booking(booking)
        except Booking.DoesNotExist:
            pass  # optional logging

    order.status = "paid"
    order.save(update_fields=["status"])