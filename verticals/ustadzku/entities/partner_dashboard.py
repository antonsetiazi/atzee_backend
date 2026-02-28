# verticals/ustadzku/entities/partner_dashboard.py

from django.utils import timezone
from django.db import models
from django.db.models import Sum, Avg

from core.entities.contracts import BaseEntity
from business.bookings.models import Booking, BookingStatus
from business.partners.models import Partner
from core.widgets.models import UIWidget


class PartnerDashboardEntity(BaseEntity):
    """
    ustadzku.partner.dashboard entity
    """

    key = "partner.dashboard"
    domain = "ustadzku"
    permission = "ustadzku.partner.dashboard.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        now = timezone.now()

        # -----------------------------------------
        # GET PARTNER
        # -----------------------------------------
        try:
            partner = Partner.objects.get(
                tenant=tenant,
                core_user=user,
            )
        except Partner.DoesNotExist:
            return {
                "today_bookings": 0,
                "upcoming_bookings_count": 0,
                "active_booking": 0,
                "total_earnings": 0.0,
                "average_rating": 0.0,
                "incoming_bookings": [],
                "active_services": [],
                "recent_services": [],
                "banners": None,
            }

        try:
            # -----------------------------------------
            # BASE QUERYSET
            # -----------------------------------------
            qs = Booking.objects.filter(
                tenant=tenant,
                partner=partner,
            )

            # -----------------------------------------
            # SUMMARY COUNTS / STATS
            # -----------------------------------------
            today_bookings = qs.filter(
                start_time__date=now.date(),
                status__in=[
                    BookingStatus.CONFIRMED,
                    BookingStatus.ON_GOING,
                    BookingStatus.PENDING_PAYMENT,
                ]
            ).count()

            upcoming_bookings_count = qs.filter(
                start_time__gt=now,
                status__in=[
                    BookingStatus.CONFIRMED,
                    BookingStatus.PENDING_PAYMENT,
                ],
            ).count()

            active_booking = qs.filter(
                status=BookingStatus.ON_GOING
            ).count()

            # -----------------------------------------
            # TOTAL PENDAPATAN BULAN INI
            # -----------------------------------------
            total_earnings = (
                Booking.objects.filter(
                    tenant=tenant,
                    partner=partner,
                    status=BookingStatus.SETTLED,
                    start_time__year=now.year,
                    start_time__month=now.month,
                    is_deleted=False,
                )
                .aggregate(total=Sum("partner_amount"))["total"]
                or 0
            )

            # -----------------------------------------
            # RATING RATA-RATA
            # -----------------------------------------
            average_rating = partner.rating_avg or 0.0
            
            # -----------------------------------------
            # LIST BOOKING MASUK (MAX 5)
            # -----------------------------------------
            incoming_qs = qs.filter(
                status__in=[BookingStatus.PENDING_PAYMENT, BookingStatus.CONFIRMED]
            ).order_by("start_time")[:5]

            incoming_bookings = [
                {
                    "id": str(b.id),
                    "booking_number": b.booking_number,
                    "user_name": str(b.user),
                    "start_time": b.start_time.isoformat(),
                    "status": b.status,
                }
                for b in incoming_qs
            ]

            # -----------------------------------------
            # LIST LAYANAN AKTIF (MAX 5)
            # -----------------------------------------
            active_qs = qs.filter(status=BookingStatus.ON_GOING).order_by("start_time")[:5]

            active_services = [
                {
                    "id": str(b.id),
                    "service_name": b.service_name,
                    "user_name": str(b.user),
                    "current_status": b.status,
                    "status": b.status,
                }
                for b in active_qs
            ]

            # -----------------------------------------
            # RIWAYAT LAYANAN (MAX 5)
            # -----------------------------------------
            recent_qs = qs.filter(
                status__in=[BookingStatus.COMPLETED, BookingStatus.SETTLED, BookingStatus.CANCELLED]
            ).order_by("-start_time")[:5]

            recent_services = [
                {
                    "id": str(b.id),
                    "booking_number": b.booking_number,
                    "user_name": str(b.user),
                    "start_time": b.start_time.isoformat(),
                    "status": b.status,
                }
                for b in recent_qs
            ]

            # -----------------------------------------
            # BANNERS
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
            # FINAL RESPONSE
            # -----------------------------------------
            return {
                "today_bookings": today_bookings,
                "upcoming_bookings_count": upcoming_bookings_count,
                "active_booking": active_booking,
                "total_earnings": float(total_earnings),
                "average_rating": round(float(average_rating), 2),
                "incoming_bookings": incoming_bookings,
                "active_services": active_services,
                "recent_services": recent_services,
                "banners": banners,
            }

        except Exception as e:
            print(e)
            return {
                "today_bookings": 0,
                "upcoming_bookings_count": 0,
                "active_booking": 0,
                "total_earnings": 0.0,
                "average_rating": 0.0,
                "incoming_bookings": [],
                "active_services": [],
                "recent_services": [],
                "banners": None,
            }