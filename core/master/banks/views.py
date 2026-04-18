# core/master/banks/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.master.banks import selectors, services
from core.master.banks.serializers import (
    BankListSerializer,
    BankDetailSerializer,
    BankCreateSerializer,
    BankUpdateSerializer,
)


class BankViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)

        active_only = request.query_params.get("all") != "1"

        qs = selectors.get_banks(
            tenant=tenant,
            active_only=active_only,
        )

        return Response(
            BankListSerializer(qs, many=True).data
        )

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        obj = selectors.get_bank_by_id(
            tenant=tenant,
            bank_id=pk,
        )

        if not obj:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            BankDetailSerializer(obj).data
        )

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = BankCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        obj = services.create_bank(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            BankDetailSerializer(obj).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = BankUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        obj = services.update_bank(
            tenant=tenant,
            bank_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            BankDetailSerializer(obj).data
        )

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_bank(
            tenant=tenant,
            bank_id=pk,
            deleted_by=request.user,
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )