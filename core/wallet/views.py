# core/wallet/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.wallet import selectors, services
from core.wallet.serializers import (
    WalletSerializer, 
    WalletTransactionSerializer, 
    WalletTopUpSerializer
)


class WalletViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        wallet = selectors.get_wallet(tenant=tenant, user=request.user)
        if not wallet:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(WalletSerializer(wallet).data)

    def list_transactions(self, request):
        tenant = TenantService.get_current_tenant(request)
        wallet = selectors.get_wallet(tenant=tenant, user=request.user)
        if not wallet:
            return Response(status=status.HTTP_404_NOT_FOUND)

        qs = selectors.get_wallet_transactions(wallet=wallet)
        return Response(WalletTransactionSerializer(qs, many=True).data)

    def top_up(self, request):
        tenant = TenantService.get_current_tenant(request)
        wallet = selectors.get_wallet(tenant=tenant, user=request.user)
        if not wallet:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WalletTopUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaction = services.credit_wallet(
            tenant=tenant,
            wallet=wallet,
            amount=serializer.validated_data["amount"],
            transaction_type="topup",
            description=serializer.validated_data.get("description", ""),
        )

        return Response(WalletTransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
    

    def pay_booking(self, request, booking_id: int):
        tenant = TenantService.get_current_tenant(request)

        from business.bookings.services.payment import pay_booking_with_wallet

        result = pay_booking_with_wallet(
            tenant=tenant,
            user=request.user,
            booking_id=booking_id
        )
        
        return Response(result)