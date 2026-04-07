# business/booking/api/views_partner_schedule.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from business.booking.models import Booking
from marketplace.models.order import Order


class PartnerScheduleAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            tenant = TenantService.get_current_tenant(request)

            if not hasattr(request.user, "partner_profile"):
                return Response([])

            partner = request.user.partner_profile

        # 🔥 ambil order milik partner
            orders = (
                Order.objects
                .filter(
                    tenant=tenant,
                    selected_partner=partner
                )
                .prefetch_related("items__listing__product")
                .order_by("created_at")
            )

            bookings = Booking.objects.filter(
                tenant=tenant
            )

            booking_map = {
                str(b.id): b for b in bookings
            }
            
            data = []

            for o in orders:
                if not o.booking_id:
                    continue

                booking = booking_map.get(str(o.booking_id))
                if not booking:
                    continue

                # 🔥 ambil item pertama
                first_item = o.items.first()

                if first_item and first_item.listing and first_item.listing.product:
                    title = first_item.listing.product.name
                else:
                    title = "Service"

                data.append({
                    "id": str(o.id),
                    "order_number": o.order_number,
                    "start_time": booking.start_time,
                    "end_time": booking.end_time,
                    "status": o.status,
                    "title": title,
                })

            return Response(data)
        except Exception as e:
            print(e)