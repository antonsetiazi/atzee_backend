# business/bookings/entities/admin_bookings_list.py

from core.entities.contracts import BaseEntity
from business.bookings.models import Booking, BookingStatus
from business.users.models import BusinessUser
from business.partners.models import Partner
from business.enum.permissions import BusinessPermission


class AdminBookingsListEntity(BaseEntity):
    """
    business.admin.bookings.list
    Admin melihat semua booking dalam tenant
    """

    key = "admin.bookings.list"
    domain = "business"
    permission = BusinessPermission.ADMIN_BOOKINGS_VIEW
    

    def query(self, *, user, tenant, query: dict) -> dict:
        try:
            # -----------------------------------------
            # BASE QUERYSET (SEMUA BOOKING TENANT)
            # -----------------------------------------
            qs = Booking.objects.filter(
                tenant=tenant,
                is_deleted=False,
            )

            # -----------------------------------------
            # FILTER: STATUS
            # -----------------------------------------
            status = query.get("status")
            if status:
                qs = qs.filter(status=status)

            # -----------------------------------------
            # FILTER: USER
            # -----------------------------------------
            user_id = query.get("user_id")
            if user_id:
                qs = qs.filter(user_id=user_id)

            # -----------------------------------------
            # FILTER: PARTNER
            # -----------------------------------------
            partner_id = query.get("partner_id")
            if partner_id:
                qs = qs.filter(partner_id=partner_id)

            # -----------------------------------------
            # FILTER: DATE RANGE
            # -----------------------------------------
            start_date = query.get("start_date")
            end_date = query.get("end_date")

            if start_date:
                qs = qs.filter(start_time__date__gte=start_date)

            if end_date:
                qs = qs.filter(start_time__date__lte=end_date)

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

                    # USER INFO
                    "user_id": str(b.user.id),
                    "user_name": str(b.user),

                    # PARTNER INFO
                    "partner_id": str(b.partner.id),
                    "partner_name": str(b.partner),

                    # SCHEDULE
                    "start_time": b.start_time.isoformat(),
                    "end_time": b.end_time.isoformat(),
                    "duration_minutes": b.duration_minutes,

                    # FINANCIAL SNAPSHOT
                    "subtotal_amount": str(b.subtotal_amount),
                    "platform_fee": str(b.platform_fee),
                    "partner_amount": str(b.partner_amount),
                    "total_price": str(b.total_price),

                    # STATUS
                    "status": b.status,
                    "payment_status": b.payment_status,
                    "is_financial_locked": b.is_financial_locked,
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