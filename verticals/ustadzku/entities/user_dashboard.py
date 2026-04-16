# verticals/ustadzku/entities/user_dashboard.py

from django.utils import timezone
from django.db import models

from core.entities.contracts import BaseEntity
from business.users.models import BusinessUser
from core.widgets.models import UIWidget

from marketplace.models.order import Order, OrderStatus
from business.booking.models import Booking, BookingStatus
from business.booking.services.booking_read_service import (
    get_partner_name_from_order
)

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
            pass

        try:

            # -----------------------------------------
            # ORDER BASE (SOURCE OF TRUTH)
            # -----------------------------------------
            orders = (
                Order.objects
                .filter(
                    tenant=tenant,
                    user=user,
                    booking_id__isnull=False,
                )
                .prefetch_related("items__listing__partner")
            )

            booking_ids = orders.values_list("booking_id", flat=True)

            bookings = Booking.objects.filter(
                tenant=tenant,
                id__in=booking_ids,
            )

            # -----------------------------------------
            # SUMMARY COUNTS
            # -----------------------------------------
            upcoming_booking = bookings.filter(
                start_time__gt=now,
                status__in=[
                    BookingStatus.HOLD,
                ],
            ).count()

            active_booking = bookings.filter(
                status=BookingStatus.COMPLETED
            ).count()

            completed_booking = bookings.filter(
                status=BookingStatus.CONFIRMED
            ).count()

            # total_booking = bookings.count()

            # -----------------------------------------
            # UPCOMING BOOKINGS (MAX 5)
            # -----------------------------------------
            upcoming_qs = bookings.filter(
                start_time__gte=now,
                status__in=[
                    BookingStatus.CONFIRMED,
                    BookingStatus.HOLD,
                ],
            ).order_by("start_time")[:5]

            upcoming_bookings = [
                {
                    "id": str(b.id),
                    "start_time": b.start_time.isoformat(),
                    "status": b.status,
                    "resource_type": b.resource_type,
                    "resource_id": b.resource_id,
                }
                for b in upcoming_qs
            ]

            # -----------------------------------------
            # MAP BOOKING → ORDER
            # -----------------------------------------
            orders_map = {
                str(o.booking_id): o
                for o in orders
            }

            # -----------------------------------------
            # RECENT BOOKINGS (ENRICHED)
            # -----------------------------------------
            recent_qs = bookings.filter(
                status__in=[
                    BookingStatus.COMPLETED,
                    BookingStatus.CANCELED,
                ]
            ).order_by("-start_time")[:5]

            recent_bookings = []

            for b in recent_qs:
                order = orders_map.get(str(b.id))

                recent_bookings.append({
                    "id": str(b.id),
                    "booking_number": order.order_number if order else f"BOOK-{b.id}",
                    "partner_name": get_partner_name_from_order(order) or "-",
                    "start_time": b.start_time.isoformat(),
                    "status": b.status,
                })

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
                # "total_booking": total_booking,
                "upcoming_bookings": upcoming_bookings,
                "recent_bookings": recent_bookings,
                "banners": banners,
            }

        except Exception as e:
            print(e)
            return self._empty()
        

    def _empty(self):
        return {
            "upcoming_booking": 0,
            "active_booking": 0,
            "completed_booking": 0,
            "total_booking": 0,
            "upcoming_bookings": [],
            "recent_bookings": [],
            "banners": None,
        }