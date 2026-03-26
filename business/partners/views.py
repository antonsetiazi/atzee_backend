# business/partners/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from datetime import datetime, timedelta
from django.utils import timezone

from core.tenants.services import TenantService
from business.partners import selectors, services
from business.partners.serializers import (
    PartnerListSerializer,
    PartnerDetailSerializer,
    PartnerCreateSerializer,
    PartnerUpdateSerializer
)

from business.partners.availability import generate_partner_daily_slots

from business.products.selectors import get_partner_offerings
from business.products.serializers import PartnerOfferingCardSerializer

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
    

    @action(detail=True, methods=["get"], url_path="availability")
    def availability(self, request, pk=None):
        """
        Get availability slots for a partner.
        Example:
        GET /api/business/partners/11/availability/
        """

        tenant = TenantService.get_current_tenant(request)
        partner = selectors.get_partner_by_id(
            tenant=tenant,
            partner_id=pk
        )

        if not partner:
            return Response(
                {"detail": "Partner not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        date_str = request.query_params.get("date")

        if not date_str:
            return Response(
                {"detail": "date query param is required (YYYY-MM-DD)."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            target_date = timezone.make_aware(
                datetime.strptime(date_str, "%Y-%m-%d")
            )
        except ValueError:
            return Response(
                {"detail": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        slots = generate_partner_daily_slots(
            partner=partner,
            target_date=target_date,
        )

        return Response({
            "date": date_str,
            "slots": slots
        })
    
    @action(detail=True, methods=["get"], url_path="services")
    def services(self, request, pk=None):
        """
        Get service offerings for a partner.

        GET /api/business/partners/{id}/services/
        """

        tenant = TenantService.get_current_tenant(request)

        partner = selectors.get_partner_by_id(
            tenant=tenant,
            partner_id=pk
        )

        if not partner:
            return Response(
                {"detail": "Partner not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        offerings = get_partner_offerings(
            tenant=tenant,
            partner_id=partner.id
        )

        serializer = PartnerOfferingCardSerializer(
            offerings,
            many=True
        )

        return Response(serializer.data)