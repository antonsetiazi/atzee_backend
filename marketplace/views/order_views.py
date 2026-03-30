# marketplace/views/order_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView

from marketplace.models.order import Order
from marketplace.serializers.order_output_serializer import OrderSerializer
from marketplace.serializers.order_serializer import CreateOrderSerializer
from core.tenants.services import TenantService


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = CreateOrderSerializer(
            data=request.data,
            context={
                "request": request,
                "tenant": tenant,
            },
        )

        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        return Response({
            "id": order.id,
            "total": int(order.total_amount),
            "status": order.status,
        })


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tenant = TenantService.get_current_tenant(self.request)

        return (
            Order.objects
            .filter(
                tenant=tenant,
                user=self.request.user,
            )
            .prefetch_related("items__listing__product")
            .order_by("-created_at")
        )


class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        tenant = TenantService.get_current_tenant(self.request)

        return (
            Order.objects
            .filter(
                tenant=tenant,
                user=self.request.user,
            )
            .prefetch_related("items__listing__product")
        )