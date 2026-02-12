# core/schedule/recurrings/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.schedule.recurrings import selectors, services
from core.schedule.recurrings.serializers import (
    RecurringListSerializer,
    RecurringDetailSerializer,
    RecurringCreateSerializer,
    RecurringUpdateSerializer,
)


class RecurringViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]


    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        recurrings = selectors.get_recurring_queryset(tenant=tenant)
        serializer = RecurringListSerializer(recurrings, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        recurring = selectors.get_recurring_by_id(
            tenant=tenant,
            recurring_id=pk
        )

        if not recurring:
            return Response(
                {"detail": "Recurring not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RecurringDetailSerializer(recurring)
        return Response(serializer.data)


    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = RecurringCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recurring = services.create_recurring(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        output = RecurringDetailSerializer(recurring)
        return Response(output.data, status=status.HTTP_201_CREATED)


    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = RecurringUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        recurring = services.update_recurring(
            tenant=tenant,
            recurring_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = RecurringDetailSerializer(recurring)
        return Response(output.data)


    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_recurring(
            tenant=tenant,
            recurring_id=pk,
            deleted_by=request.user
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

