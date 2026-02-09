# core/geo/countries/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.geo.countries import selectors, services
from core.geo.countries.serializers import (
    CountryListSerializer,
    CountryDetailSerializer,
    CountryCreateSerializer,
    CountryUpdateSerializer,
)


class CountryViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        qs = selectors.get_countries(tenant=tenant)
        return Response(CountryListSerializer(qs, many=True).data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        obj = selectors.get_country_by_id(
            tenant=tenant,
            country_id=pk
        )
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(CountryDetailSerializer(obj).data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = CountryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.create_country(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )
        return Response(
            CountryDetailSerializer(obj).data,
            status=status.HTTP_201_CREATED
        )


    def partial_update(self, request, pk=None):
        try:
            tenant = TenantService.get_current_tenant(request)
            country = selectors.get_country_by_id(
                tenant=tenant,
                country_id=pk
            )

            if not country:
                return Response(
                    {"detail": "Country not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = CountryUpdateSerializer(
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)

            country = services.update_country(
                tenant=tenant,
                country_id=country.id,
                updated_by=request.user,
                **serializer.validated_data
            )

            output = CountryDetailSerializer(country)
            return Response(output.data)
        except Exception as e:
            print(e)

    
    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_country(
            tenant=tenant,
            country_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )