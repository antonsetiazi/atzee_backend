# core/geo/regions/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.geo.regions import selectors, services
from core.geo.regions.serializers import (
    RegionListSerializer,
    RegionDetailSerializer,
    RegionCreateSerializer,
    RegionUpdateSerializer,
)


class RegionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        country_id = request.query_params.get("country_id")

        qs = selectors.get_regions(
            country_id=country_id,
        )

        return Response(
            RegionListSerializer(qs, many=True).data
        )

    def retrieve(self, request, pk=None):
        region = selectors.get_region_by_id(
            region_id=pk
        )
        if not region:
            return Response(
                {"detail": "Region not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(RegionDetailSerializer(region).data)

    def create(self, request):
        serializer = RegionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        region = services.create_region(
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            RegionDetailSerializer(region).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request, pk=None):
        serializer = RegionUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        region = services.update_region(
            region_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            RegionDetailSerializer(region).data
        )

    def destroy(self, request, pk=None):

        services.delete_region(
            region_id=pk,
            deleted_by=request.user,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
