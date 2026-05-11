# accounting/api/payable_payments/views.py

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import PayablePayment
from accounting.services.payable_payment_service import PayablePaymentService
from core.tenants.services import TenantService

from .serializers import (
    PayablePaymentCreateSerializer,
    PayablePaymentReadSerializer,
)


class PayablePaymentListAPIView(APIView):
    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        qs = PayablePayment.objects.filter(tenant=tenant)

        partner_id = request.GET.get("partner")

        if partner_id:
            qs = qs.filter(partner_id=partner_id)

        qs = qs.order_by("-payment_date", "-created_at")[:100]

        data = PayablePaymentReadSerializer(qs, many=True).data

        return Response(data)


class PayablePaymentCreateAPIView(APIView):
    def post(self, request):

        try:
            tenant = TenantService.get_current_tenant(request)
            serializer = PayablePaymentCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            payment = PayablePaymentService.create_payment(
                tenant=tenant,
                user=request.user,
                partner_id=serializer.validated_data["partner_id"],
                payment_number=serializer.validated_data["payment_number"],
                payment_date=serializer.validated_data["payment_date"],
                amount=serializer.validated_data["amount"],
                payment_method=serializer.validated_data["payment_method"],
                reference=serializer.validated_data.get("reference", ""),
                notes=serializer.validated_data.get("notes", ""),
                allocations=serializer.validated_data["allocations"],
            )

            output = PayablePaymentReadSerializer(payment)

            return Response(output.data, status=status.HTTP_201_CREATED)

        except Exception as e:

            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class PayablePaymentDetailAPIView(APIView):
    def get(self, request, payment_id):

        try:
            tenant = TenantService.get_current_tenant(request)
            payment = PayablePayment.objects.get(id=payment_id, tenant=tenant)

            data = PayablePaymentReadSerializer(payment).data

            return Response(data)

        except PayablePayment.DoesNotExist:

            return Response(
                {"error": "Payment not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class PayablePaymentPostAPIView(APIView):
    def post(self, request, payment_id):
        tenant = TenantService.get_current_tenant(request)

        payment = get_object_or_404(
            PayablePayment,
            id=payment_id,
            tenant=tenant,
        )

        try:
            payment = PayablePaymentService.post_payment(
                payment=payment,
                user=request.user,
            )

            data = PayablePaymentReadSerializer(payment).data
            return Response(data)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
