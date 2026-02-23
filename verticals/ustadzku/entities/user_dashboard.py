# verticals/ustadzku/entities/user_dashboard.py

from django.utils import timezone

from core.entities.contracts import BaseEntity
from business.bookings.models import Booking, BookingStatus


class UserDashboardEntity(BaseEntity):
    """
    ustadzku.user.dashboard entity
    """

    key = "user.dashboard"
    domain = "ustadzku"
    permission = "ustadzku.user.dashboard.view"

    def query(self, *, user, tenant, query: dict) -> dict:

        now = timezone.now()

        # ---------------------------------------
        # BASE QUERYSET (TENANT + USER SAFE)
        # ---------------------------------------
        qs = Booking.objects.filter(
            tenant=tenant,
            user=user,
        )

        # ---------------------------------------
        # SUMMARY
        # ---------------------------------------

        upcoming_count = qs.filter(
            start_time__gt=now,
            status__in=[
                BookingStatus.CONFIRMED,
                BookingStatus.PENDING_PAYMENT,
            ],
        ).count()

        active_count = qs.filter(
            status=BookingStatus.ON_GOING
        ).count()

        completed_count = qs.filter(
            status__in=[
                BookingStatus.COMPLETED,
                BookingStatus.SETTLED,
            ]
        ).count()

        total_count = qs.count()

        # ---------------------------------------
        # UPCOMING BOOKINGS (LIMIT 5)
        # ---------------------------------------

        upcoming_bookings = qs.filter(
            start_time__gte=now,
            status__in=[
                BookingStatus.CONFIRMED,
                BookingStatus.PENDING_PAYMENT,
            ],
        ).order_by("start_time")[:5]

        upcoming_list = [
            {
                "id": str(b.id),
                "booking_number": b.booking_number,
                "partner_name": str(b.partner),
                "start_time": b.start_time.isoformat(),
                "end_time": b.end_time.isoformat(),
                "duration_minutes": b.duration_minutes,
                "total_price": str(b.total_price),
                "status": b.status,
                "payment_status": b.payment_status,
            }
            for b in upcoming_bookings
        ]

        # ---------------------------------------
        # RECENT BOOKINGS (LIMIT 5)
        # ---------------------------------------

        recent_bookings = qs.filter(
            status__in=[
                BookingStatus.COMPLETED,
                BookingStatus.CANCELLED,
                BookingStatus.SETTLED,
            ]
        ).order_by("-start_time")[:5]

        recent_list = [
            {
                "id": str(b.id),
                "booking_number": b.booking_number,
                "partner_name": str(b.partner),
                "start_time": b.start_time.isoformat(),
                "total_price": str(b.total_price),
                "status": b.status,
            }
            for b in recent_bookings
        ]

        # ---------------------------------------
        # FINAL RESPONSE
        # ---------------------------------------

        return {
            "summary": {
                "bookings": {
                    "upcoming": upcoming_count,
                    "active": active_count,
                    "completed": completed_count,
                    "total": total_count,
                }
            },
            "lists": {
                "upcoming_bookings": upcoming_list,
                "recent_bookings": recent_list,
            },
            "meta": {
                "generated_at": now.isoformat(),
            }
        }