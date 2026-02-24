# business/bookings/services/lifecycle.py

from django.db import transaction
from rest_framework.exceptions import ValidationError

from business.bookings.models import Booking, BookingStatus


VALID_TRANSITIONS = {
    BookingStatus.PENDING_PAYMENT: [BookingStatus.CONFIRMED, BookingStatus.CANCELLED],
    BookingStatus.CONFIRMED: [BookingStatus.ON_GOING, BookingStatus.CANCELLED],
    BookingStatus.ON_GOING: [BookingStatus.COMPLETED],
    BookingStatus.COMPLETED: [BookingStatus.SETTLED],
}


def _change_status(booking: Booking, new_status: str):
    allowed = VALID_TRANSITIONS.get(booking.status, [])
    if new_status not in allowed:
        raise ValidationError(
            f"Invalid transition from {booking.status} to {new_status}"
        )

    booking.status = new_status
    booking.save(update_fields=["status", "updated_at"])


@transaction.atomic
def confirm_booking(booking: Booking):
    _change_status(booking, BookingStatus.CONFIRMED)

    booking.is_financial_locked = True
    booking.save(update_fields=[
        "status",
        "is_financial_locked",
        "updated_at"
    ])


@transaction.atomic
def start_booking(booking: Booking):
    _change_status(booking, BookingStatus.ON_GOING)


@transaction.atomic
def complete_booking(booking: Booking):
    _change_status(booking, BookingStatus.COMPLETED)


@transaction.atomic
def settle_booking(booking: Booking):
    _change_status(booking, BookingStatus.SETTLED)
