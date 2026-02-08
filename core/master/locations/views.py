# core/master/locations/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.master.locations import selectors, services
from core.master.locations.serializers import (
    LocationListSerializer,
    LocationDetailSerializer,
    LocationCreateSerializer,
    LocationUpdateSerializer,
)


class LocationViewSet(viewsets.ViewSet):
    """
    Location management (CORE MASTER).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        locations = selectors.get_locations(tenant=tenant)
        serializer = LocationListSerializer(locations, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        location = selectors.get_location_by_id(
            tenant=tenant,
            location_id=pk
        )

        if not location:
            return Response(
                {"detail": "Location not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            LocationDetailSerializer(location).data
        )

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = LocationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        location = services.create_location(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        return Response(
            LocationDetailSerializer(location).data,
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = LocationUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        location = services.update_location(
            tenant=tenant,
            location_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )

        return Response(
            LocationDetailSerializer(location).data
        )

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_location(
            tenant=tenant,
            location_id=pk,
            deleted_by=request.user
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
