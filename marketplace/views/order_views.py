# marketplace/views/order_views.py

from decimal import Decimal
from core.account.selectors import get_user_address_by_id
from business.partners.selectors import get_partner_by_id
from math import radians, sin, cos, sqrt, atan2

from django.core.exceptions import ValidationError

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
from marketplace.services.order_partner_service import mark_order_completed_by_partner
from marketplace.services.order_start_service import start_order
from core.tenants.services import TenantService

from core.notifications.services import NotificationService
from core.notifications.events import (
    ORDER_CREATED,
    ORDER_NEEDS_APPROVAL,
)

from core.fees.services.fee_engine import FeeEngine
from core.fees.types import FeeInput


class OrderPreviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tenant = TenantService.get_current_tenant(request)

        items = request.data.get("items", [])
        partner_id = request.data.get("selected_partner_id")
        address_id = request.data.get("address_id")
        fulfillment_type = request.data.get("fulfillment_type", "on_site")

        if not items:
            return Response({"error": "Items kosong"}, status=400)

        # =========================
        # HITUNG SUBTOTAL
        # =========================
        subtotal = Decimal("0")

        transport_fee = Decimal("0")
        distance_km = Decimal("0")

        partner = get_partner_by_id(
            tenant=tenant,
            partner_id=partner_id
        )

        address = None
        if address_id:
            address = get_user_address_by_id(
                tenant=tenant,
                user=request.user,
                address_id=address_id
            )

        if (
            partner
            and address
            and fulfillment_type == "on_site"
            and partner.search_latitude is not None
            and partner.search_longitude is not None
            and address.latitude is not None
            and address.longitude is not None
        ):
            def calc(lat1, lon1, lat2, lon2):
                r = 6371
                dlat = radians(lat2 - lat1)
                dlon = radians(lon2 - lon1)

                a = (
                    sin(dlat / 2) ** 2
                    + cos(radians(lat1))
                    * cos(radians(lat2))
                    * sin(dlon / 2) ** 2
                )

                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                return r * c

            km = calc(
                float(partner.search_latitude),
                float(partner.search_longitude),
                float(address.latitude),
                float(address.longitude),
            )

            distance_km = Decimal(str(round(km, 2)))

            if km > 3:
                transport_fee = Decimal(str(km - 3)) * Decimal("2500")

                
        for item in items:
            price = Decimal(str(item.get("price", 0)))
            qty = int(item.get("qty", 1))
            subtotal += price * qty

        # =========================
        # FEE ENGINE
        # =========================
        engine = FeeEngine()

        result = engine.calculate(
            FeeInput(
                tenant_id=str(tenant.id),
                amount=subtotal,
                partner_id=partner_id,
            )
        )

        fees = [
            {
                "name": f.name,
                "amount": int(f.amount),
            }
            for f in result.customer_fees
        ]

        # Tambahkan transport fee ke breakdown
        if transport_fee > 0:
            fees.append({
                "name": f"Biaya Transport ({distance_km} km)",
                "amount": int(transport_fee),
            })


        return Response({
            "subtotal": int(subtotal),

            "platform_fee": int(result.total_customer_fee),
            "transport_fee": int(transport_fee),
            "distance_km": float(distance_km),

            "fees": fees,

            "total_fee": int(
                result.total_customer_fee + transport_fee
            ),
            "total": int(
                result.final_customer_pay + transport_fee
            ),
        })
    

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

        # ==================================================
        # 🔔 CUSTOMER NOTIFICATION
        # ==================================================
        NotificationService.notify(
            user=request.user,
            tenant=tenant,
            event=ORDER_CREATED,
            title="Pesanan berhasil dibuat",
            message="Pesanan Anda berhasil dibuat dan menunggu persetujuan partner.",
            entity_type="order",
            entity_id=str(order.id),
        )

        # ==================================================
        # 🔔 PARTNER NOTIFICATION
        # ==================================================
        if (
            order.selected_partner
            and order.selected_partner.core_user
        ):
            NotificationService.notify(
                user=order.selected_partner.core_user,
                tenant=tenant,
                event=ORDER_NEEDS_APPROVAL,
                title="Order Baru Masuk",
                message="Ada pesanan baru yang menunggu persetujuan Anda.",
                entity_type="order",
                entity_id=str(order.id),
            )

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
    

class PartnerCompleteOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        tenant = TenantService.get_current_tenant(request)

        if not hasattr(request.user, "partner_profile"):
            return Response({"detail": "Not a partner"}, status=403)

        partner = request.user.partner_profile

        try:
            order = mark_order_completed_by_partner(
                tenant=tenant,
                order_id=id,
                partner=partner
            )

            return Response({
                "success": True,
                "status": order.status,
            })

        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )    
        

class StartOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        tenant = TenantService.get_current_tenant(request)

        if not hasattr(request.user, "partner_profile"):
            return Response({"detail": "Not a partner"}, status=403)

        partner = request.user.partner_profile

        try:
            order = start_order(
                tenant=tenant,
                order_id=id,
                partner=partner
            )

            return Response({
                "success": True,
                "status": order.status,
            })

        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )        