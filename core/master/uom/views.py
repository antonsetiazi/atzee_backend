# core/master/uom/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.master.uom import selectors, services
from core.master.uom.serializers import (
    UOMListSerializer,
    UOMDetailSerializer,
    UOMCreateSerializer,
    UOMUpdateSerializer,
)


class UOMViewSet(viewsets.ViewSet):
    """
    Unit of Measure management (CORE MASTER).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        uoms = selectors.get_uoms(tenant=tenant)
        serializer = UOMListSerializer(uoms, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        uom = selectors.get_uom_by_id(
            tenant=tenant,
            uom_id=pk
        )

        if not uom:
            return Response(
                {"detail": "UOM not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            UOMDetailSerializer(uom).data
        )

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = UOMCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uom = services.create_uom(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        output = UOMDetailSerializer(uom)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
            

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        uom = selectors.get_uom_by_id(
            tenant=tenant,
            uom_id=pk
        )

        if not uom:
            return Response(
                {"detail": "UOM not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UOMUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        uom = services.update_uom(
            tenant=tenant,
            uom=uom,
            updated_by=request.user,
            **serializer.validated_data
        )

        return Response(
            UOMDetailSerializer(uom).data
        )


    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        uom = selectors.get_uom_by_id(
            tenant=tenant,
            uom_id=pk
        )

        if not uom:
            return Response(
                {"detail": "UOM not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UOMUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        uom = services.update_uom(
            tenant=tenant,
            uom_id=uom.id,
            updated_by=request.user,
            **serializer.validated_data
        )
    
        output = UOMDetailSerializer(uom)
        return Response(output.data)
    

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_uom(
            tenant=tenant,
            uom_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )