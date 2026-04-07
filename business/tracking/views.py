# business/tracking/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService

from business.tracking import services
from business.tracking import selectors
from marketplace.models.order import Order


class UpdateLocationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tenant = TenantService.get_current_tenant(request)

        partner = request.user.partner_profile

        lat = request.data.get("latitude")
        lng = request.data.get("longitude")

        services.update_partner_location(
            tenant=tenant,
            partner=partner,
            latitude=lat,
            longitude=lng
        )

        return Response({"success": True})
    

class OrderTrackingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        tenant = TenantService.get_current_tenant(request)

        order = Order.objects.filter(
            tenant=tenant,
            id=order_id,
            user=request.user
        ).first()

        if not order or not hasattr(order, "tracking"):
            return Response({"detail": "Tracking not available"}, status=404)

        tracking = order.tracking

        location = selectors.get_latest_partner_location(
            tenant=tenant,
            partner=tracking.partner
        )

        return Response({
            "partner_id": tracking.partner.id,
            "location": {
                "latitude": location.latitude if location else None,
                "longitude": location.longitude if location else None,
            },
            "destination": order.address_snapshot
        })    