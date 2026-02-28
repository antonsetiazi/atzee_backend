# business/bookings/entities/partner_bookings_upcoming.py

from django.utils import timezone

from core.entities.contracts import BaseEntity
from business.bookings.models import Booking, BookingStatus
from business.partners.models import Partner


class PartnerBookingsUpcomingEntity(BaseEntity):
    """
    business.partner.bookings.upcoming
    """

    key = "partner.bookings.upcoming"
    domain = "business"
    permission = "business.partner.bookings.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        # -----------------------------------------
        # GET BUSINESS PARTNER
        # -----------------------------------------
        try:
            partner = Partner.objects.get(
                tenant=tenant,
                core_user=user,
            )
        except Partner.DoesNotExist:
            return {
                "items": [],
                "total": 0,
            }

        try:
            now = timezone.now()

            # -----------------------------
            # BASE QUERYSET
            # -----------------------------
            qs = Booking.objects.filter(
                tenant=tenant,
                partner=partner,
                start_time__gte=now,
                status__in=[
                    BookingStatus.PENDING_PAYMENT,
                    BookingStatus.CONFIRMED,
                ],
            )

            # -----------------------------
            # SEARCH (booking_number)
            # -----------------------------
            search = query.get("search")
            if search:
                qs = qs.filter(booking_number__icontains=search)

            # -----------------------------
            # PAGINATION
            # -----------------------------
            page = int(query.get("page", 1))
            page_size = int(query.get("pageSize", 10))

            offset = (page - 1) * page_size
            limit = offset + page_size

            total = qs.count()
            items = qs.order_by("start_time")[offset:limit]

            # -----------------------------
            # SERIALIZE
            # -----------------------------
            data = [
                {
                    "id": str(b.id),
                    "booking_number": b.booking_number,
                    "user_name": str(b.user),
                    "start_time": b.start_time.isoformat(),
                    "end_time": b.end_time.isoformat(),
                    "duration_minutes": b.duration_minutes,
                    "partner_amount": str(b.partner_amount),
                    "status": b.status,
                    "payment_status": b.payment_status,
                }
                for b in items
            ]

            return {
                "items": data,
                "total": total,
            }

        except Exception as e:
            print(e)
            return {
                "items": [],
                "total": 0,
            }