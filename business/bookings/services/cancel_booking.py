# business/bookings/services/cancel_booking.py

from django.db import transaction
from rest_framework.exceptions import ValidationError

from business.bookings.models import Booking, BookingStatus


@transaction.atomic
def cancel_booking(booking: Booking, reason: str = ""):

    if booking.status not in [
        BookingStatus.PENDING_PAYMENT,
        BookingStatus.CONFIRMED
    ]:
        raise ValidationError("Cannot cancel this booking.")

    booking.status = BookingStatus.CANCELLED
    booking.extensions = booking.extensions or {}
    booking.extensions["cancel_reason"] = reason
    booking.save(update_fields=["status", "extensions", "updated_at"])
