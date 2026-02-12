# core/schedule/reminders/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.schedule.reminders import selectors, services, serializers


class ReminderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        reminders = selectors.get_reminder_queryset(tenant=tenant)
        serializer = serializers(reminders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        reminder = selectors.get_reminder_by_id(tenant=tenant, reminder_id=pk)
        if not reminder:
            return Response({"detail": "Reminder not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers(reminder)
        return Response(serializer.data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = serializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        reminder = services.create_reminder(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )
        output = serializers(reminder)
        return Response(output.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        reminder = selectors.get_reminder_by_id(tenant=tenant, reminder_id=pk)
        if not reminder:
            return Response({"detail": "Reminder not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        reminder = services.update_reminder(
            tenant=tenant,
            reminder_id=reminder.id,
            updated_by=request.user,
            **serializer.validated_data
        )
        output = serializers(reminder)
        return Response(output.data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        services.delete_reminder(tenant=tenant, reminder_id=pk, deleted_by=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
