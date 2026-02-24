# business/bookings/services/cancel_booking.py

from django.db import transaction
from rest_framework.exceptions import ValidationError

from business.bookings.models import Booking, BookingStatus


@transaction.atomic
def cancel_booking(booking: Booking, reason: str = ""):

    if booking.status == BookingStatus.PENDING_PAYMENT:
        booking.status = BookingStatus.CANCELLED

    elif booking.status == BookingStatus.CONFIRMED:
        # TODO: trigger refund logic here
        booking.status = BookingStatus.CANCELLED

    else:
        raise ValidationError("Cannot cancel this booking.")

    booking.extensions = booking.extensions or {}
    booking.extensions["cancel_reason"] = reason

    booking.save(update_fields=[
        "status",
        "extensions",
        "updated_at"
    ])
