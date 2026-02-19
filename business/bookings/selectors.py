# business/bookings/selectors.py

from typing import Optional
from django.db.models import QuerySet
from django.utils import timezone

from core.tenants.models import Tenant
from business.bookings.models import Booking


def get_booking_queryset(*, tenant: Tenant) -> QuerySet[Booking]:
    return Booking.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_booking_by_id(*, tenant: Tenant, booking_id: int) -> Optional[Booking]:
    try:
        return get_booking_queryset(tenant=tenant).get(id=booking_id)
    except Booking.DoesNotExist:
        return None


def get_partner_active_bookings(
    *, tenant: Tenant, partner_id: int, start_time, end_time
) -> QuerySet[Booking]:
    """
    Used for availability validation.
    """
    return (
        get_booking_queryset(tenant=tenant)
        .filter(
            partner_id=partner_id,
            status__in=["CONFIRMED", "ON_GOING"],
            start_time__lt=end_time,
            end_time__gt=start_time
        )
    )
