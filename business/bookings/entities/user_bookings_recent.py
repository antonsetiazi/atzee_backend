# business/bookings/entities/user_bookings_recent.py

from core.entities.contracts import BaseEntity
from business.bookings.models import Booking, BookingStatus
from business.users.models import BusinessUser

class UserBookingsRecentEntity(BaseEntity):
    """
    business.user.bookings.recent
    """

    key = "user.bookings.recent"
    domain = "business"
    permission = "business.user.bookings.view"

    def query(self, *, user, tenant, query: dict) -> dict:

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
                "items": [],
                "total": 0,
            }

        # -----------------------------------------
        # BASE QUERYSET
        # -----------------------------------------
        try:
            qs = Booking.objects.filter(
                tenant=tenant,
                user=business_user,
                status__in=[
                    BookingStatus.COMPLETED,
                    BookingStatus.CANCELLED,
                    BookingStatus.SETTLED,
                ],
            )
        except Exception as e:
            print(e)

        # -----------------------------------------
        # SEARCH (booking_number)
        # -----------------------------------------
        search = query.get("search")
        if search:
            qs = qs.filter(booking_number__icontains=search)

        # -----------------------------------------
        # PAGINATION
        # -----------------------------------------
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()

        items = qs.order_by("-start_time")[offset:limit]

        # -----------------------------------------
        # SERIALIZE
        # -----------------------------------------
        data = [
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
            for b in items
        ]

        return {
            "items": data,
            "total": total,
        }