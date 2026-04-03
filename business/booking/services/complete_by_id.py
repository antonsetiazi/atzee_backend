# business/booking/services/complete_by_id.py

from django.db import transaction

from business.booking.models import Booking
from business.booking.services.complete import complete_booking


@transaction.atomic
def complete_booking_by_id(booking_id):

    booking = (
        Booking.objects
        .select_for_update()
        .filter(id=booking_id)
        .first()
    )

    if not booking:
        raise ValueError("Booking tidak ditemukan")

    return complete_booking(booking)