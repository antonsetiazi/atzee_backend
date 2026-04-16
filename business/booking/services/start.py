# business/booking/services/start.py

from django.db import transaction
from django.core.exceptions import ValidationError

from business.booking.models import Booking, BookingStatus


@transaction.atomic
def start_booking(booking: Booking):
    """
    Mark booking as ONGOING

    RULE:
    - hanya CONFIRMED yang boleh start
    """

    if booking.status != BookingStatus.CONFIRMED:
        raise ValidationError("Booking belum bisa dimulai")

    booking.status = BookingStatus.ONGOING
    booking.save(update_fields=["status", "updated_at"])

    return booking