# marketplace/views/order_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status

from marketplace.models.order import Order
from marketplace.serializers.order_output_serializer import OrderSerializer
from marketplace.serializers.order_serializer import CreateOrderSerializer
from marketplace.services.order_completion_service import complete_order
from marketplace.services.order_assignment_service import (
    assign_partner_to_order, 
    accept_order, 
    reject_order
)
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
            "payment_status": order.payment_status,
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
    

class CompleteOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        try:
            order = complete_order(order_id=id, user=request.user)

            return Response({
                "success": True,
                "status": order.status,
            })

        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        except PermissionError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_403_FORBIDDEN
            )    
        

class AssignPartnerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        tenant = TenantService.get_current_tenant(request)

        partner_id = request.data.get("partner_id")

        order = assign_partner_to_order(
            tenant=tenant,
            order_id=id,
            partner_id=partner_id
        )

        return Response({
            "success": True,
            "partner_id": order.partner.id
        })        
    

class AcceptOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        tenant = TenantService.get_current_tenant(request)

        if not hasattr(request.user, "partner_profile"):
            return Response({"detail": "Not a partner"}, status=403)

        partner = request.user.partner_profile

        order = accept_order(
            tenant=tenant,
            order_id=id,
            partner=partner
        )

        return Response({
            "success": True,
            "order_id": order.id
        })    
    

class RejectOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        tenant = TenantService.get_current_tenant(request)

        if not hasattr(request.user, "partner_profile"):
            return Response({"detail": "Not a partner"}, status=403)

        reason = request.data.get("reason", "")

        partner = request.user.partner_profile

        reject_order(
            tenant=tenant,
            order_id=id,
            partner=partner,
            reason=reason
        )

        return Response({"success": True})    