# core/schedule/shifts/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.schedule.shifts import selectors, services
from core.schedule.shifts.serializers import (
    ShiftListSerializer,
    ShiftDetailSerializer,
    ShiftCreateSerializer,
    ShiftUpdateSerializer,
)


class ShiftViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]


    def list(self, request):
        tenant = TenantService.get_current_tenant(request)

        queryset = selectors.get_shift_queryset(tenant=tenant)
        serializer = ShiftListSerializer(queryset, many=True)

        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        shift = selectors.get_shift_by_id(
            tenant=tenant,
            shift_id=int(pk),
        )

        if not shift:
            return Response(
                {"detail": "Shift not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ShiftDetailSerializer(shift)
        return Response(serializer.data)


    def create(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = ShiftCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        shift = services.create_shift(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data,
        )

        output = ShiftDetailSerializer(shift)
        return Response(output.data, status=status.HTTP_201_CREATED)
            

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = ShiftUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        shift = services.update_shift(
            tenant=tenant,
            shift_id=int(pk),
            updated_by=request.user,
            **serializer.validated_data,
        )

        output = ShiftDetailSerializer(shift)
        return Response(output.data)
            

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = ShiftUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        shift = services.update_shift(
            tenant=tenant,
            shift_id=int(pk),
            updated_by=request.user,
            **serializer.validated_data,
        )

        output = ShiftDetailSerializer(shift)
        return Response(output.data)


    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_shift(
            tenant=tenant,
            shift_id=int(pk),
            deleted_by=request.user,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
