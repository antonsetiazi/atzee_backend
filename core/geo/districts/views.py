# core/geo/districts/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.geo.districts import selectors, services
from core.geo.districts.serializers import (
    DistrictListSerializer,
    DistrictDetailSerializer,
    DistrictCreateSerializer,
    DistrictUpdateSerializer,
)


class DistrictViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        country_id = request.query_params.get("country_id")
        region_id = request.query_params.get("region_id")
        city_id = request.query_params.get("city_id")

        qs = selectors.get_districts(
            country_id=int(country_id) if country_id else None,
            region_id=int(region_id) if region_id else None,
            city_id=int(city_id) if city_id else None,
        )

        return Response(
            DistrictListSerializer(qs, many=True).data
        )

    def retrieve(self, request, pk=None):
        district = selectors.get_district_by_id(pk)

        if not district:
            return Response(
                {"detail": "District not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            DistrictDetailSerializer(district).data
        )

    def create(self, request):
        serializer = DistrictCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        district = services.create_district(
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            DistrictDetailSerializer(district).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request, pk=None):
        serializer = DistrictUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        district = services.update_district(
            district_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            DistrictDetailSerializer(district).data
        )

    def destroy(self, request, pk=None):
        services.delete_district(
            district_id=pk,
            deleted_by=request.user,
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )