# core/geo/spatial/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.geo.spatial import selectors, services
from core.geo.spatial.serializers import (
    GeoLocationListSerializer,
    GeoLocationDetailSerializer,
    GeoLocationCreateSerializer,
    GeoLocationUpdateSerializer
)


class GeoLocationViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)

        related_entity = request.query_params.get("related_entity")
        related_id = request.query_params.get("related_id")

        if not related_entity or not related_id:
            return Response(
                {"detail": "related_entity and related_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        qs = selectors.get_locations_by_relation(
            tenant=tenant,
            related_entity=related_entity,
            related_id=related_id
        )

        serializer = GeoLocationListSerializer(qs, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        obj = selectors.get_location_by_id(
            tenant=tenant,
            location_id=pk
        )

        if not obj:
            return Response(
                {"detail": "Location not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GeoLocationDetailSerializer(obj)
        return Response(serializer.data)


    def create(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = GeoLocationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.create_location(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        output = GeoLocationDetailSerializer(obj)
        return Response(output.data, status=status.HTTP_201_CREATED)


    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = GeoLocationUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        obj = services.update_location(
            tenant=tenant,
            location_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = GeoLocationDetailSerializer(obj)
        return Response(output.data)


    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_location(
            tenant=tenant,
            location_id=pk,
            deleted_by=request.user
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
