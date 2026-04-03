# business/booking/services/complete.py

from django.db import transaction
from django.utils import timezone

from business.booking.models import Booking, BookingStatus


@transaction.atomic
def complete_booking(booking: Booking):
    """
    Mark booking as COMPLETED

    RULE:
    - hanya CONFIRMED / ONGOING yang boleh selesai
    """

    if booking.status not in [
        BookingStatus.CONFIRMED,
        BookingStatus.ONGOING,
    ]:
        raise ValueError("Booking tidak bisa diselesaikan")

    booking.status = BookingStatus.COMPLETED
    booking.save(update_fields=["status", "updated_at"])

    return booking