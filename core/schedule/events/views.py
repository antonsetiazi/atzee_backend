# core/schedule/events/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.schedule.events import selectors, services
from core.schedule.events.serializers import (
    EventCreateSerializer,
    EventUpdateSerializer,
    EventDetailSerializer,
    EventListSerializer, 
)


class EventViewSet(viewsets.ViewSet):
    """
    Event API endpoints (tenant-scoped).
    """

    permission_classes = [IsAuthenticated]


    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        events = selectors.get_event_queryset(tenant=tenant)
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        event = selectors.get_event_by_id(tenant=tenant, event_id=pk)
        if not event:
            return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)


    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = EventCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        event = services.create_event(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        output = EventDetailSerializer(event)
        return Response(output.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        event = selectors.get_event_by_id(tenant=tenant, event_id=pk)
        if not event:
            return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        event = services.update_event(
            tenant=tenant,
            event_id=event.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = EventDetailSerializer(event)
        return Response(output.data)


    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        event = selectors.get_event_by_id(tenant=tenant, event_id=pk)
    
        if not event:
            return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventUpdateSerializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        event = services.update_event(
            tenant=tenant,
            event_id=event.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = EventDetailSerializer(event)
        return Response(output.data)


    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        event = selectors.get_event_by_id(tenant=tenant, event_id=pk)
        if not event:
            return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        services.delete_event(tenant=tenant, event_id=pk, deleted_by=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
