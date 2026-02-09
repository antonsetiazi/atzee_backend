# core/geo/timezones/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.geo.timezones import selectors, services
from core.geo.timezones.serializers import (
    TimezoneListSerializer,
    TimezoneDetailSerializer,
    TimezoneCreateSerializer,
    TimezoneUpdateSerializer,
)


class TimezoneViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        qs = selectors.get_timezones(tenant=tenant)
        return Response(TimezoneListSerializer(qs, many=True).data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        obj = selectors.get_timezone_by_id(
            tenant=tenant,
            timezone_id=pk,
        )
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(TimezoneDetailSerializer(obj).data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = TimezoneCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.create_timezone(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            TimezoneDetailSerializer(obj).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = TimezoneUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        obj = services.update_timezone(
            tenant=tenant,
            timezone_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(TimezoneDetailSerializer(obj).data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_timezone(
            tenant=tenant,
            timezone_id=pk,
            deleted_by=request.user,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
