# core/master/currencies/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.master.currencies import selectors, services
from core.master.currencies.serializers import (
    CurrencyListSerializer,
    CurrencyDetailSerializer,
    CurrencyCreateSerializer,
    CurrencyUpdateSerializer,
)


class CurrencyViewSet(viewsets.ViewSet):
    """
    Currency master management (CORE).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        currencies = selectors.get_currencies(tenant=tenant)
        return Response(
            CurrencyListSerializer(currencies, many=True).data
        )

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        currency = selectors.get_currency_by_id(
            tenant=tenant,
            currency_id=pk
        )

        if not currency:
            return Response(
                {"detail": "Currency not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            CurrencyDetailSerializer(currency).data
        )

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = CurrencyCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        currency = services.create_currency(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        return Response(
            CurrencyDetailSerializer(currency).data,
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = CurrencyUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        currency = services.update_currency(
            tenant=tenant,
            currency_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )

        return Response(
            CurrencyDetailSerializer(currency).data
        )
