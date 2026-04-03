# business/booking/services/query.py

from business.booking.models import Booking


def get_user_bookings(tenant, user):
    """
    Ambil semua booking milik user
    """

    return Booking.objects.filter(
        tenant=tenant,
        created_by=user
    ).order_by("-start_time")


def get_booking_detail(tenant, user, booking_id):
    return Booking.objects.get(
        id=booking_id,
        tenant=tenant,
        created_by=user
    )