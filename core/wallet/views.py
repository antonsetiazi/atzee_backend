# core/wallet/views.py

from decimal import Decimal
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from core.tenants.services import TenantService
from core.wallet import selectors, services
from core.wallet.serializers import (
    WalletSerializer,
    WalletTransactionSerializer,
    WalletTopUpSerializer
)
import uuid


class WalletViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    # ==============================
    # GET WALLET
    # ==============================
    def list(self, request):
        tenant = TenantService.get_current_tenant(request)

        wallet = selectors.get_wallet_or_create(
            tenant=tenant,
            user=request.user
        )

        return Response(WalletSerializer(wallet).data)

    # ==============================
    # GET TRANSACTIONS
    # ==============================
    @action(detail=False, methods=["get"], url_path="transactions")
    def transactions(self, request):
        tenant = TenantService.get_current_tenant(request)

        wallet = selectors.get_wallet_or_create(
            tenant=tenant,
            user=request.user
        )

        limit = int(request.query_params.get("limit", 50))

        qs = selectors.get_wallet_transactions(
            tenant=tenant,
            wallet=wallet,
            limit=limit
        )

        return Response(
            WalletTransactionSerializer(qs, many=True).data
        )

    # ==============================
    # TOPUP (SIMULATION / MANUAL)
    # ==============================
    @action(detail=False, methods=["post"], url_path="topup")
    def topup(self, request):
        tenant = TenantService.get_current_tenant(request)

        wallet = selectors.get_wallet_or_create(
            tenant=tenant,
            user=request.user
        )

        serializer = WalletTopUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount: Decimal = serializer.validated_data["amount"]

        tx = services.topup_wallet(
            tenant=tenant,
            wallet=wallet,
            amount=amount,
            idempotency_key=f"topup-{uuid.uuid4()}",
            description=serializer.validated_data.get("description", ""),
        )

        return Response(
            WalletTransactionSerializer(tx).data,
            status=status.HTTP_201_CREATED
        )