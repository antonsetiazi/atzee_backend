# business/booking/services/cancel.py

from django.db import transaction
from django.utils import timezone

from business.booking.models import Booking, BookingStatus


@transaction.atomic
def cancel_booking(booking: Booking):
    now = timezone.now()

    # 🔥 Handle expired HOLD
    if (
        booking.status == BookingStatus.HOLD and
        booking.expires_at and
        booking.expires_at < now
    ):
        booking.status = BookingStatus.EXPIRED
        booking.save(update_fields=["status", "updated_at"])
        raise ValueError("Booking already expired")

    if booking.status not in [
        BookingStatus.HOLD,
        BookingStatus.CONFIRMED,
    ]:
        raise ValueError("Cannot cancel this booking")

    booking.status = BookingStatus.CANCELED
    booking.save(update_fields=["status", "updated_at"])

    return booking