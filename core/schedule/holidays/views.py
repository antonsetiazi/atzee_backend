# core/schedule/views/holiday_views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.schedule.holidays import selectors, services, serializers


class HolidayViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        holidays = selectors.get_holiday_queryset(tenant=tenant)
        serializer = serializers(holidays, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        holiday = selectors.get_holiday_by_id(tenant=tenant, holiday_id=pk)
        if not holiday:
            return Response({"detail": "Holiday not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers(holiday)
        return Response(serializer.data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = serializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        holiday = services.create_holiday(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )
        output = serializers(holiday)
        return Response(output.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        holiday = selectors.get_holiday_by_id(tenant=tenant, holiday_id=pk)
        if not holiday:
            return Response({"detail": "Holiday not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        holiday = services.update_holiday(
            tenant=tenant,
            holiday_id=holiday.id,
            updated_by=request.user,
            **serializer.validated_data
        )
        output = serializers(holiday)
        return Response(output.data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        services.delete_holiday(tenant=tenant, holiday_id=pk, deleted_by=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
