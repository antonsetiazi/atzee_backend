# verticals/ustadzku/entities/user_dashboard.py

from django.utils import timezone
from django.db import models

from core.entities.contracts import BaseEntity
from business.bookings.models import Booking, BookingStatus
from business.users.models import BusinessUser
from core.widgets.models import UIWidget


class UserDashboardEntity(BaseEntity):
    """
    ustadzku.user.dashboard entity
    """

    key = "user.dashboard"
    domain = "ustadzku"
    permission = "ustadzku.user.dashboard.view"

    def query(self, *, user, tenant, query: dict) -> dict:

        now = timezone.now()

        # -----------------------------------------
        # GET BUSINESS USER
        # -----------------------------------------
        try:
            business_user = BusinessUser.objects.get(
                tenant=tenant,
                core_user=user,
            )
        except BusinessUser.DoesNotExist:
            return {
                "upcoming_booking": 0,
                "active_booking": 0,
                "completed_booking": 0,
                "total_booking": 0,
                "upcoming_bookings": [],
                "recent_bookings": [],
                "banners": None,
            }

        try:
            # -----------------------------------------
            # BASE QUERYSET
            # -----------------------------------------
            qs = Booking.objects.filter(
                tenant=tenant,
                user=business_user,
            )

            # -----------------------------------------
            # SUMMARY COUNTS
            # -----------------------------------------
            upcoming_booking = qs.filter(
                start_time__gt=now,
                status__in=[
                    BookingStatus.CONFIRMED,
                    BookingStatus.PENDING_PAYMENT,
                ],
            ).count()

            active_booking = qs.filter(
                status=BookingStatus.ON_GOING
            ).count()

            completed_booking = qs.filter(
                status__in=[
                    BookingStatus.COMPLETED,
                    BookingStatus.SETTLED,
                ]
            ).count()

            total_booking = qs.count()

            # -----------------------------------------
            # UPCOMING BOOKINGS (MAX 5)
            # -----------------------------------------
            upcoming_qs = qs.filter(
                start_time__gte=now,
                status__in=[
                    BookingStatus.CONFIRMED,
                    BookingStatus.PENDING_PAYMENT,
                ],
            ).order_by("start_time")[:5]

            upcoming_bookings = [
                {
                    "id": str(b.id),
                    "booking_number": b.booking_number,
                    "partner_name": str(b.partner),
                    "start_time": b.start_time.isoformat(),
                    "status": b.status,
                }
                for b in upcoming_qs
            ]

            # -----------------------------------------
            # RECENT BOOKINGS (MAX 5)
            # -----------------------------------------
            recent_qs = qs.filter(
                status__in=[
                    BookingStatus.COMPLETED,
                    BookingStatus.CANCELLED,
                    BookingStatus.SETTLED,
                ]
            ).order_by("-start_time")[:5]

            recent_bookings = [
                {
                    "id": str(b.id),
                    "booking_number": b.booking_number,
                    "partner_name": str(b.partner),
                    "start_time": b.start_time.isoformat(),
                    "status": b.status,
                }
                for b in recent_qs
            ]

            # -----------------------------------------
            # BANNERS (FROM UIWidget)
            # -----------------------------------------
            widget_qs = UIWidget.objects.filter(
                tenant=tenant,
                type="banner",
                is_deleted=False,
                is_active=True,
            ).filter(
                models.Q(starts_at__isnull=True) | models.Q(starts_at__lte=now)
            ).filter(
                models.Q(ends_at__isnull=True) | models.Q(ends_at__gte=now)
            ).order_by("order")

            banners = []

            for w in widget_qs:
                config = w.config or {}

                if isinstance(config, list):
                    config = config[0] if config else {}

                banners.append({
                    "id": str(w.id),
                    "title": w.title,
                    "image_url": config.get("image_url"),
                    "link_url": config.get("link_url"),
                    "open_in_new_tab": config.get("open_in_new_tab", True),
                })

            # -----------------------------------------
            # FINAL RESPONSE (FLAT STRUCTURE)
            # -----------------------------------------
            return {
                "upcoming_booking": upcoming_booking,
                "active_booking": active_booking,
                "completed_booking": completed_booking,
                "total_booking": total_booking,
                "upcoming_bookings": upcoming_bookings,
                "recent_bookings": recent_bookings,
                "banners": banners,
            }

        except Exception as e:
            print(e)
            return {
                "upcoming_booking": 0,
                "active_booking": 0,
                "completed_booking": 0,
                "total_booking": 0,
                "upcoming_bookings": [],
                "recent_bookings": [],
                "banners": None,
            }