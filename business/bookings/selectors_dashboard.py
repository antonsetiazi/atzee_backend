# business/bookings/selectors_dashboard.py

from django.utils import timezone
from django.db.models import QuerySet

from core.tenants.models import Tenant
from business.bookings.models import Booking, BookingStatus
from business.users.models import BusinessUser


def get_user_booking_queryset(*, tenant: Tenant, user: BusinessUser) -> QuerySet[Booking]:
    return Booking.objects.filter(
        tenant=tenant,
        user=user,
        is_deleted=False
    )


def get_user_upcoming_bookings(*, tenant: Tenant, user: BusinessUser) -> QuerySet[Booking]:
    now = timezone.now()

    return (
        get_user_booking_queryset(tenant=tenant, user=user)
        .filter(
            start_time__gt=now,
            status__in=[
                BookingStatus.PENDING_PAYMENT,
                BookingStatus.CONFIRMED
            ]
        )
        .order_by("start_time")
    )


def get_user_active_bookings(*, tenant: Tenant, user: BusinessUser) -> QuerySet[Booking]:
    return (
        get_user_booking_queryset(tenant=tenant, user=user)
        .filter(status=BookingStatus.ON_GOING)
        .order_by("-start_time")
    )


def get_user_recent_bookings(*, tenant: Tenant, user: BusinessUser) -> QuerySet[Booking]:
    return (
        get_user_booking_queryset(tenant=tenant, user=user)
        .filter(status__in=[
            BookingStatus.COMPLETED,
            BookingStatus.CANCELLED,
            BookingStatus.SETTLED
        ])
        .order_by("-start_time")[:5]
    )


def get_user_total_booking_count(*, tenant: Tenant, user: BusinessUser) -> int:
    return get_user_booking_queryset(tenant=tenant, user=user).count()