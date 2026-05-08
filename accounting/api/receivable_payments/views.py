# accounting/api/receivable_payments/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import ReceivablePayment
from accounting.services.receivable_payment_service import (
    ReceivablePaymentService,
)
from core.tenants.services import TenantService

from .serializers import (
    ReceivablePaymentCreateSerializer,
    ReceivablePaymentSerializer,
)


class ReceivablePaymentListAPIView(APIView):

    def get(self, request):

        tenant = TenantService.get_current_tenant(request)
        qs = ReceivablePayment.objects.filter(tenant=tenant)

        customer_id = request.GET.get("customer")

        if customer_id:
            qs = qs.filter(customer_id=customer_id)

        qs = qs.order_by("-payment_date", "-created_at")[:100]

        data = ReceivablePaymentSerializer(qs, many=True).data

        return Response(data)


class ReceivablePaymentCreateAPIView(APIView):

    def post(self, request):

        try:

            tenant = TenantService.get_current_tenant(request)

            serializer = ReceivablePaymentCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            payment = ReceivablePaymentService.create_payment(
                tenant=tenant,
                user=request.user,
                customer_id=serializer.validated_data["customer_id"],
                payment_number=serializer.validated_data["payment_number"],
                payment_date=serializer.validated_data["payment_date"],
                payment_method=serializer.validated_data["payment_method"],
                amount=serializer.validated_data["amount"],
                allocations=serializer.validated_data["allocations"],
                notes=serializer.validated_data.get("notes", ""),
            )

            output = ReceivablePaymentSerializer(payment)

            return Response(output.data, status=status.HTTP_201_CREATED)

        except Exception as e:

            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class ReceivablePaymentDetailAPIView(APIView):

    def get(self, request, payment_id):

        try:
            tenant = TenantService.get_current_tenant(request)

            payment = ReceivablePayment.objects.get(
                id=payment_id, tenant=tenant
            )

            data = ReceivablePaymentSerializer(payment).data

            return Response(data)

        except ReceivablePayment.DoesNotExist:

            return Response(
                {"error": "Payment not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
