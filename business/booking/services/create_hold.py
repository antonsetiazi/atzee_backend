# business/booking/services/create_hold.py

from datetime import timedelta
from django.db import transaction
from django.utils import timezone
from django.db.models import Q

from business.booking.models import Booking, BookingStatus


HOLD_DURATION_MINUTES = 10


def create_hold_booking(
    *,
    tenant,
    resource_type: str,
    resource_id,
    start_time,
    end_time,
    order_id=None,
    meta: dict = None,
    created_by=None,
):
    """
    Create HOLD booking (SESSION-BASED)

    RULE:
    - 1 Order = 1 Booking
    - Booking wajib punya order_id (no orphan)
    - Booking = lock resource + time
    """

    if end_time <= start_time:
        raise ValueError("Invalid time range")

    now = timezone.now()

    with transaction.atomic():

        # 🔒 LOCK candidate rows (prevent race condition)
        conflicting_qs = (
            Booking.objects
            .select_for_update()
            .filter(
                tenant=tenant,
                resource_type=resource_type,
                resource_id=resource_id,
                start_time__lt=end_time,
                end_time__gt=start_time,
            )
        )

        # 🔥 FILTER hanya booking yang benar-benar blocking
        conflicting_qs = conflicting_qs.filter(
            Q(status__in=[
                BookingStatus.CONFIRMED,
                BookingStatus.ONGOING,
            ]) |
            Q(
                status=BookingStatus.HOLD,
                expires_at__gt=now
            )
        )

        if conflicting_qs.exists():
            raise ValueError("Time slot not available")

        # ⏱ Freeze duration
        duration = int((end_time - start_time).total_seconds() / 60)

        # ⏳ TTL HOLD
        expires_at = now + timedelta(minutes=HOLD_DURATION_MINUTES)

        booking = Booking.objects.create(
            tenant=tenant,
            resource_type=resource_type,
            resource_id=resource_id,
            start_time=start_time,
            end_time=end_time,
            total_duration=duration,
            status=BookingStatus.HOLD,
            expires_at=expires_at,
            order_id=order_id,
            meta=meta or {},
            created_by=created_by,
        )

        return booking