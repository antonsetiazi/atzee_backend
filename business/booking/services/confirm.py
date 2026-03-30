# business/booking/services/confirm.py

from django.db import transaction
from django.utils import timezone
from django.db.models import Q

from business.booking.models import Booking, BookingStatus


@transaction.atomic
def confirm_booking(booking: Booking):
    now = timezone.now()

    if booking.status != BookingStatus.HOLD:
        raise ValueError("Only HOLD booking can be confirmed")

    # 🔥 Expired check
    if booking.expires_at and booking.expires_at < now:
        booking.status = BookingStatus.EXPIRED
        booking.save(update_fields=["status", "updated_at"])
        raise ValueError("Booking expired")

    # 🔒 Re-check conflict (VERY IMPORTANT)
    conflicting = (
        Booking.objects
        .select_for_update()
        .filter(
            tenant=booking.tenant,
            resource_type=booking.resource_type,
            resource_id=booking.resource_id,
            start_time__lt=booking.end_time,
            end_time__gt=booking.start_time,
        )
        .exclude(id=booking.id)
        .filter(
            Q(status__in=[
                BookingStatus.CONFIRMED,
                BookingStatus.ONGOING,
            ]) |
            Q(
                status=BookingStatus.HOLD,
                expires_at__gt=now
            )
        )
    )

    if conflicting.exists():
        raise ValueError("Time slot already taken")

    booking.status = BookingStatus.CONFIRMED
    booking.save(update_fields=["status", "updated_at"])

    return booking