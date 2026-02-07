# accounting/fiscal_period/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from accounting.fiscal_period import selectors, services, serializers
from core.permissions.access.accounting import IsAccountingAdmin
from core.tenants.services import TenantService


class FiscalPeriodViewSet(viewsets.ViewSet):
    """
    CRUD + Read fiscal periods + Close (tenant scoped)
    """

    permission_classes = [IsAuthenticated, IsAccountingAdmin]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        queryset = selectors.get_fiscal_period_queryset(tenant=tenant)
        serializer = serializers.FiscalPeriodListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        period = selectors.get_fiscal_period_by_id(tenant=tenant, period_id=pk)
        if not period:
            return Response({"detail": "Fiscal period not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.FiscalPeriodDetailSerializer(period)
        return Response(serializer.data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = serializers.FiscalPeriodCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        period = services.create_fiscal_period(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )
        output = serializers.FiscalPeriodDetailSerializer(period)
        return Response(output.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = serializers.FiscalPeriodUpdateSerializer(data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        period = services.update_fiscal_period(
            tenant=tenant,
            period_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )
        output = serializers.FiscalPeriodDetailSerializer(period)
        return Response(output.data)

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = serializers.FiscalPeriodUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        period = services.update_fiscal_period(
            tenant=tenant,
            period_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )
        output = serializers.FiscalPeriodDetailSerializer(period)
        return Response(output.data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        period = selectors.get_fiscal_period_by_id(tenant=tenant, period_id=pk)
        if not period:
            return Response({"detail": "Fiscal period not found."}, status=status.HTTP_404_NOT_FOUND)
        if period.is_closed:
            return Response({"detail": "Cannot delete closed fiscal period."}, status=status.HTTP_400_BAD_REQUEST)
        period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["post"], url_path="close")
    def close_period(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        try:
            period = services.close_fiscal_period(tenant=tenant, period_id=pk, closed_by=request.user)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": f"Fiscal period '{period.name}' closed successfully."})
