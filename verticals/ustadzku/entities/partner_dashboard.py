# verticals/ustadzku/entities/partner_dashboard.py

from django.utils import timezone
from django.db import models
from django.db.models import Sum

from core.entities.contracts import BaseEntity
from business.partners.models import Partner
from core.widgets.models import UIWidget

from marketplace.models.order import Order, OrderStatus, PaymentStatus
from business.booking.models import Booking

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
            return self._empty()

        # print(partner.id)
        # print(partner.name)
        try:

            # -----------------------------------------
            # ORDER BASE (🔥 SOURCE OF TRUTH)
            # -----------------------------------------
            orders = (
                Order.objects
                .filter(
                    tenant=tenant,
                    partner=partner,  # 🔥 FIX UTAMA
                    booking_id__isnull=False,
                )
                .select_related("user")
                .order_by("-created_at")
            )

            booking_ids = orders.values_list("booking_id", flat=True)

            bookings = Booking.objects.filter(
                tenant=tenant,
                id__in=booking_ids,
            )

            booking_map = {
                str(b.id): b
                for b in bookings
            }

            # -----------------------------------------
            # 📊 STATS (ORDER-BASED)
            # -----------------------------------------

            # 🔥 Booking hari ini
            today_bookings = bookings.filter(
                start_time__date=now.date()
            ).count()

            # 🔥 Upcoming (future schedule)
            upcoming_bookings_count = bookings.filter(
                start_time__gt=now
            ).count()

            # 🔥 Active (order sedang berjalan)
            active_booking = orders.filter(
                status__in=[
                    OrderStatus.ACCEPTED,
                    OrderStatus.ON_GOING,
                ]
            ).count()


            # -----------------------------------------
            # 💰 EARNINGS (VALID)
            # -----------------------------------------
            total_earnings = (
                orders.filter(
                    payment_status=PaymentStatus.PAID,
                    status=OrderStatus.COMPLETED,
                    paid_at__year=now.year,
                    paid_at__month=now.month,
                )
                .aggregate(total=Sum("total_amount"))["total"]
                or 0
            )

            # -----------------------------------------
            # 📥 INCOMING ORDERS
            # -----------------------------------------
            incoming_qs = orders.filter(
                status=OrderStatus.PENDING
            )[:5]

            incoming_bookings = []

            for o in incoming_qs:
                b = booking_map.get(str(o.booking_id))

                incoming_bookings.append({
                    "id": str(o.id),
                    "booking_number": o.order_number,
                    "user_name": str(o.user),
                    "start_time": b.start_time.isoformat() if b else None,
                    "status": o.status,
                })

            # -----------------------------------------
            # 🚀 ACTIVE SERVICES
            # -----------------------------------------
            active_qs = orders.filter(
                status__in=[
                    OrderStatus.ACCEPTED,
                    OrderStatus.ON_GOING,
                ]
            )[:5]

            active_services = []

            for o in active_qs:
                b = booking_map.get(str(o.booking_id))

                active_services.append({
                    "id": str(o.id),
                    "service_name": "Layanan",
                    "user_name": str(o.user),
                    "current_status": o.status,
                    "status": o.status,
                })

            # -----------------------------------------
            # 🧾 RECENT SERVICES
            # -----------------------------------------
            recent_qs = orders.filter(
                status__in=[
                    OrderStatus.COMPLETED,
                    OrderStatus.CANCELLED,
                ]
            )[:5]

            recent_services = []

            for o in recent_qs:
                b = booking_map.get(str(o.booking_id))

                recent_services.append({
                    "id": str(o.id),
                    "booking_number": o.order_number,
                    "user_name": str(o.user),
                    "start_time": b.start_time.isoformat() if b else None,
                    "status": o.status,
                })


            # -----------------------------------------
            # ⭐ RATING
            # -----------------------------------------
            average_rating = round(float(partner.rating_avg or 0), 2)


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
            data = {
                "today_bookings": today_bookings,
                "upcoming_bookings_count": upcoming_bookings_count,
                "active_booking": active_booking,
                "total_earnings": float(total_earnings),
                "average_rating": average_rating,
                "incoming_bookings": incoming_bookings,
                "active_services": active_services,
                "recent_services": recent_services,
                "banners": banners,
            }

            # print(data)
        
            return data

        except Exception as e:
            print(e)
            return self._empty()
        
    def _empty(self):
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