# marketplace/views/partner_order_views.py

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView

from marketplace.models.order import Order
from marketplace.serializers.order_output_serializer import OrderSerializer
from core.tenants.services import TenantService


class PartnerOrderListView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tenant = TenantService.get_current_tenant(self.request)

        if not hasattr(self.request.user, "partner_profile"):
            return Order.objects.none()

        partner = self.request.user.partner_profile

        return (
            Order.objects
            .filter(
                tenant=tenant,
                # 🔥 CORE LOGIC
                selected_partner=partner,  # order masuk ke dia
            )
            .prefetch_related("items__listing__product")
            .order_by("-created_at")
        )
    

class PartnerOrderDetailView(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        tenant = TenantService.get_current_tenant(self.request)

        if not hasattr(self.request.user, "partner_profile"):
            return Order.objects.none()

        partner = self.request.user.partner_profile

        return (
            Order.objects
            .filter(
                tenant=tenant,
                selected_partner=partner,
            )
            .prefetch_related("items__listing__product")
        )    