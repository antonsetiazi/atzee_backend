# business/bookings/views.py

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.utils import timezone

from core.tenants.services import TenantService
from business.bookings import selectors
from business.bookings.serializers import (
    BookingListSerializer,
    BookingDetailSerializer,
    BookingCreateSerializer
)
from business.bookings.services.create_booking import create_booking
from business.bookings.models import Booking
from business.partners.models import Partner
from business.users.models import BusinessUser
from business.products.models import PartnerProduct

class BookingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        bookings = selectors.get_booking_queryset(tenant=tenant)
        return Response(BookingListSerializer(bookings, many=True).data)


    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        booking = (
            selectors.get_booking_queryset(tenant=tenant)
            .select_related("user", "partner")
            .prefetch_related("items__product")
            .filter(id=pk)
            .first()
        )

        if not booking:
            return Response({"detail": "Not found."}, status=404)

        return Response(BookingDetailSerializer(booking).data)


    def create(self, request):
        try:
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
                items=serializer.validated_data["items"],
                location_address=serializer.validated_data.get("location_address"),
                location_lat=serializer.validated_data.get("location_lat"),
                location_lng=serializer.validated_data.get("location_lng"),
            )

            return Response(
                BookingDetailSerializer(booking).data,
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(e)


    @action(detail=False, methods=["get"], url_path="context")
    def context(self, request):
        tenant = TenantService.get_current_tenant(request)

        partner_id = request.query_params.get("partner_id")
        if not partner_id:
            return Response(
                {"detail": "partner_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        partner = get_object_or_404(
            Partner,
            id=partner_id,
            tenant=tenant,
            is_deleted=False
        )

        # 🔥 Ambil layanan milik partner lewat PartnerProduct
        partner_products = PartnerProduct.objects.filter(
            tenant=tenant,
            partner=partner,
            is_active=True,
        ).select_related("product")

        return Response({
            "partner": {
                "id": partner.id,
                "name": partner.name,
            },
            "services": [
                {
                    "id": pp.product.id,
                    "name": pp.product.name,
                    "price": str(pp.price),
                    "duration_minutes": pp.duration_minutes,
                }
                for pp in partner_products
            ]
        })
    
    
    @action(detail=False, methods=["post"], url_path="estimate")
    def estimate(self, request):
        tenant = TenantService.get_current_tenant(request)

        partner_id = request.data.get("partner_id")
        service_ids = request.data.get("services", [])

        if not partner_id or not service_ids:
            return Response(
                {"detail": "partner_id and services required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        partner_products = PartnerProduct.objects.filter(
            tenant=tenant,
            partner_id=partner_id,
            product_id__in=service_ids,
            is_active=True,
        )

        subtotal = sum([pp.price for pp in partner_products])
        platform_fee = 0
        total = subtotal + platform_fee

        return Response({
            "subtotal": str(subtotal),
            "platform_fee": str(platform_fee),
            "total": str(total),
        })
    

    @action(detail=False, methods=["get"], url_path="availability")
    def availability(self, request):
        tenant = TenantService.get_current_tenant(request)

        partner_id = request.query_params.get("partner_id")
        date = request.query_params.get("date")
        service_ids = request.query_params.get("service_ids")

        if not partner_id or not date or not service_ids:
            return Response(
                {"detail": "partner_id, date, service_ids required"},
                status=400
            )

        service_ids = service_ids.split(",")

        partner_products = PartnerProduct.objects.filter(
            tenant=tenant,
            partner_id=partner_id,
            product_id__in=service_ids,
            is_active=True
        )

        total_duration = sum(pp.duration_minutes for pp in partner_products)

        # contoh sederhana 9–17
        from datetime import datetime, timedelta, time

        date_obj = datetime.fromisoformat(date)

        naive_start = datetime.combine(date_obj, time(9, 0))
        naive_end = datetime.combine(date_obj, time(17, 0))

        start_of_day = timezone.make_aware(naive_start)
        end_of_day = timezone.make_aware(naive_end)

        slots = []
        current = start_of_day

        while current + timedelta(minutes=total_duration) <= end_of_day:
            slot_end = current + timedelta(minutes=total_duration)

            conflict = Booking.objects.filter(
                tenant=tenant,
                partner_id=partner_id,
                start_time__lt=slot_end,
                end_time__gt=current,
                is_deleted=False,
            ).exists()

            slots.append({
                "start": current.isoformat(),
                "end": slot_end.isoformat(),
                "available": not conflict
            })

            current += timedelta(minutes=30)

        return Response({
            "date": date,
            "slots": slots
        })