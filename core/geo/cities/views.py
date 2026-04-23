# core/geo/cities/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.geo.cities import selectors, services
from core.geo.cities.serializers import (
    CityListSerializer,
    CityDetailSerializer,
    CityCreateSerializer,
)


class CityViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        country_id = request.query_params.get("country_id")
        region_id = request.query_params.get("region_id")

        qs = selectors.get_cities(
            country_id=country_id,
            region_id=region_id,
        )

        return Response(
            CityListSerializer(qs, many=True).data
        )

    def retrieve(self, request, pk=None):
        city = selectors.get_city_by_id(
            city_id=pk
        )
        if not city:
            return Response(
                {"detail": "City not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(CityDetailSerializer(city).data)

    def create(self, request):
        serializer = CityCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        city = services.create_city(
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            CityDetailSerializer(city).data,
            status=status.HTTP_201_CREATED,
        )
