# business/partners/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from business.partners import selectors, services
from business.partners.serializers import (
    PartnerListSerializer,
    PartnerDetailSerializer,
    PartnerCreateSerializer,
    PartnerUpdateSerializer
)


class PartnerViewSet(viewsets.ViewSet):
    """
    Partner API endpoints (tenant-scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        partners = selectors.get_partners(tenant=tenant)
        serializer = PartnerListSerializer(partners, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        partner = selectors.get_partner_by_id(tenant=tenant, partner_id=pk)

        if not partner:
            return Response(
                {"detail": "Partner not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = PartnerDetailSerializer(partner)
        return Response(serializer.data)
    

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = PartnerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        partner =services.create_partner(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        output = PartnerDetailSerializer(partner)
        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
    

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        partner = selectors.get_partner_by_id(tenant=tenant, partner_id=pk)

        if not partner:
            return Response(
                {"detail": "Partner not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = PartnerUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        partner = services.update_partner(
            tenant=tenant,
            partner_id=partner.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = PartnerDetailSerializer(partner)
        return Response(output.data)
    

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        partner = selectors.get_partner_by_id(tenant=tenant, partner_id=pk)

        if not partner:
            return Response(
                {"detail": "Partner not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = PartnerUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        partner = services.update_partner(
            tenant=tenant,
            partner_id=partner.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = PartnerDetailSerializer(partner)
        return Response(output.data)
    

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_partner(
            tenant=tenant,
            partner_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )