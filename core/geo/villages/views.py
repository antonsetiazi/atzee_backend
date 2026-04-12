# core/geo/villages/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.geo.villages import selectors, services
from core.geo.villages.serializers import (
    VillageListSerializer,
    VillageDetailSerializer,
    VillageCreateSerializer,
    VillageUpdateSerializer,
)


class VillageViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        qs = selectors.get_villages(
            country_id=request.query_params.get("country_id"),
            region_id=request.query_params.get("region_id"),
            city_id=request.query_params.get("city_id"),
            district_id=request.query_params.get("district_id"),
        )

        return Response(
            VillageListSerializer(qs, many=True).data
        )

    def retrieve(self, request, pk=None):
        village = selectors.get_village_by_id(pk)

        if not village:
            return Response(
                {"detail": "Village not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            VillageDetailSerializer(village).data
        )

    def create(self, request):
        serializer = VillageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        village = services.create_village(
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            VillageDetailSerializer(village).data,
            status=status.HTTP_201_CREATED,
        )