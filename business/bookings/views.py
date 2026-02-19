# business/bookings/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from business.bookings import selectors
from business.bookings.serializers import (
    BookingListSerializer,
    BookingDetailSerializer,
    BookingCreateSerializer
)
from business.bookings.services.create_booking import create_booking
from business.partners.models import Partner
from business.users.models import BusinessUser


class BookingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        bookings = selectors.get_booking_queryset(tenant=tenant)
        return Response(BookingListSerializer(bookings, many=True).data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        booking = selectors.get_booking_by_id(tenant=tenant, booking_id=pk)

        if not booking:
            return Response({"detail": "Not found."}, status=404)

        return Response(BookingDetailSerializer(booking).data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = BookingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = BusinessUser.objects.get(id=serializer.validated_data["user_id"])
        partner = Partner.objects.get(id=serializer.validated_data["partner_id"])

        booking = create_booking(
            tenant=tenant,
            created_by=request.user,
            user=user,
            partner=partner,
            start_time=serializer.validated_data["start_time"],
            end_time=serializer.validated_data["end_time"],
            location_address=serializer.validated_data.get("location_address"),
            location_lat=serializer.validated_data.get("location_lat"),
            location_lng=serializer.validated_data.get("location_lng"),
        )

        return Response(
            BookingDetailSerializer(booking).data,
            status=status.HTTP_201_CREATED
        )
