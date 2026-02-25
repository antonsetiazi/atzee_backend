# core/payment/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.payment import selectors, services
from core.payment.serializers import PaymentSerializer, PaymentCreateSerializer


class PaymentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        payments = selectors.get_payments_by_user(tenant=tenant, user=request.user)
        return Response(PaymentSerializer(payments, many=True).data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        payment = selectors.get_payment_by_id(tenant=tenant, payment_id=pk)
        if not payment:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(PaymentSerializer(payment).data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = PaymentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment = services.create_payment(
            tenant=tenant,
            user=request.user,
            method_code=serializer.validated_data["method_code"],
            amount=serializer.validated_data["amount"],
            reference=serializer.validated_data.get("reference", ""),
            description=serializer.validated_data.get("description", ""),
        )

        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)