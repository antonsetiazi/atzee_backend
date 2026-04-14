# business/booking/entities/booking_list.py

from core.entities.contracts import BaseEntity
from business.booking.models import Booking

from django.utils.timezone import localtime
from business.enum.permissions import BusinessPermission


class BookingListEntity(BaseEntity):
    key = "bookings.list"
    domain = "business"
    permission = BusinessPermission.ADMIN_BOOKINGS_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = Booking.objects.filter(
            tenant=tenant,
        )

        # 🔍 SEARCH
        search = query.get("search")
        if search:
            qs = qs.filter(resource_id__icontains=search)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = []
        for b in items:
            data.append({
                "id": str(b.id),

                # 🔥 resource
                "resource_type": b.resource_type,
                "resource_id": b.resource_id,

                # ⏱️ time (localized biar enak di UI)
                "start_time": localtime(b.start_time),
                "end_time": localtime(b.end_time),

                # ⏳ duration
                "total_duration": b.total_duration or 0,

                # 🔄 status
                "status": b.status,
            })

        return {
            "items": data,
            "total": total,
        }