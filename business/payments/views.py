# business/payments/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from business.payments import selectors, services
from business.payments.serializers import (
    PaymentListSerializer,
    PaymentDetailSerializer,
    PaymentCreateSerializer,
)


class PaymentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]


    def list(self, request):
        payments = selectors.get_payments(
            tenant=request.tenant
        )
        serializer = PaymentListSerializer(payments, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        payment = selectors.get_payment_by_id(
            tenant=request.tenant,
            payment_id=pk
        )

        if not payment:
            return Response(
                {"detail": "Payment not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = PaymentDetailSerializer(payment)
        return Response(serializer.data)
    

    def create(self, request):
        serializer = PaymentCreateSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        payment = serializer.save()
        output = PaymentDetailSerializer(payment)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
    
    
    def post(self, request, pk=None):
        payment = services.post_payment(
            tenant=request.tenant,
            payment_id=pk,
            posted_by=request.user
        )
        return Response(PaymentDetailSerializer(payment).data)
    

    def destroy(self, request, pk=None):
        services.void_payment(
            tenant=request.tenant,
            payment_id=pk,
            voided_by=request.user
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
