# business/booking/services/expire.py

from django.utils import timezone

from business.booking.models import Booking, BookingStatus


def expire_bookings():
    now = timezone.now()

    qs = Booking.objects.filter(
        status=BookingStatus.HOLD,
        expires_at__lt=now
    )

    updated_count = qs.update(
        status=BookingStatus.EXPIRED,
        updated_at=now
    )

    return updated_count