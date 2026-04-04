# business/payment_gateway/views_payment.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from business.payment_gateway.services.gateway_service import create_payment
from business.payment_gateway.models import PaymentMethod
from marketplace.models import Order


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_payment_view(request):
    try:
        tenant = request.tenant

        order_id = request.data.get("order_id")
        method_code = request.data.get("payment_method")

        if not order_id:
            return Response(
                {"error": "order_id wajib"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔗 ambil order
        order = get_object_or_404(
            Order,
            id=order_id,
            tenant=tenant
        )

        method = None

        if method_code:
            method = get_object_or_404(
                PaymentMethod,
                tenant=tenant,
                code=method_code,
                is_active=True
            )
        else:
            # 🔥 AUTO PICK DEFAULT (Midtrans Snap case)
            method = PaymentMethod.objects.filter(
                tenant=tenant,
                is_active=True
            ).first()

            if not method:
                return Response(
                    {"error": "Metode pembayaran tidak tersedia"},
                    status=status.HTTP_400_BAD_REQUEST
                )
    
        # 💰 create payment gateway
        payment = create_payment(
            tenant=tenant,
            reference_type="order",
            reference_id=str(order.id),
            amount=order.total_amount,
            provider=method.provider,
            channel=method.code
        )

        return Response({
            "order_id": str(order.id),
            "payment_url": payment.payment_url,
            "payment_token": payment.payment_token,
            "status": payment.status,
        })
    
    except Exception as e:
        print(e)