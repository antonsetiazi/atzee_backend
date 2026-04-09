# business/booking/api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from datetime import datetime

from core.tenants.services import TenantService
from business.booking.services.create_hold import create_hold_booking
from business.booking.services.confirm import confirm_booking
from business.booking.services.cancel import cancel_booking
from business.booking.services.availability import get_availability
from business.booking.models import Booking
from business.reviews.models import Review

from .serializers import CreateHoldBookingSerializer

from business.booking.services.query import (
    get_user_bookings,
    get_booking_detail,
)


class CreateBookingHoldAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            tenant = TenantService.get_current_tenant(request)

            serializer = CreateHoldBookingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            booking = create_hold_booking(
                tenant=tenant,
                resource_type=serializer.validated_data["resource_type"],
                resource_id=serializer.validated_data["resource_id"],
                start_time=serializer.validated_data["start_time"],
                end_time=serializer.validated_data["end_time"],
                order_id=None,  # 🔥 BELUM ADA ORDER
                meta=serializer.validated_data.get("meta"),
                created_by=request.user,
            )

            return Response({
                "booking_id": str(booking.id),
                "status": booking.status,
                "expires_at": booking.expires_at,
            })
        except Exception as e:
            print(e)
    

class ConfirmBookingAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, booking_id):
        tenant = TenantService.get_current_tenant(request)

        booking = Booking.objects.get(
            id=booking_id,
            tenant=tenant
        )

        confirm_booking(booking)

        return Response({
            "status": "confirmed"
        })

    

class CancelBookingAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, booking_id):
        tenant = TenantService.get_current_tenant(request)

        booking = Booking.objects.get(
            id=booking_id,
            tenant=tenant
        )

        cancel_booking(booking)

        return Response({
            "status": "canceled"
        })
    

class AvailabilityAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        resource_type = request.query_params.get("resource_type")
        resource_id = request.query_params.get("resource_id")
        date_str = request.query_params.get("date")
        duration = request.query_params.get("duration")

        if not all([resource_type, resource_id, date_str, duration]):
            return Response({"error": "Missing params"}, status=400)

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            duration = int(duration)
        except Exception:
            return Response({"error": "Invalid date or duration"}, status=400)

        data = get_availability(
            tenant=tenant,
            resource_type=resource_type,
            resource_id=resource_id,
            date=date,
            duration_minutes=duration,
        )

        return Response(data)   
    

class MyBookingListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        bookings = get_user_bookings(
            tenant=tenant,
            user=request.user
        )

        data = [
            {
                "id": str(b.id),
                "resource_id": b.resource_id,
                "start_time": b.start_time,
                "end_time": b.end_time,
                "status": b.status,
            }
            for b in bookings
        ]

        return Response(data)    
    

class BookingDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, booking_id):
        tenant = TenantService.get_current_tenant(request)

        booking = get_booking_detail(
            tenant=tenant,
            user=request.user,
            booking_id=booking_id
        )

        has_reviewed = hasattr(booking, "review")

        can_review = (
            booking.status == "COMPLETED"
            and not has_reviewed
        )

        data = {
            "id": str(booking.id),
            "resource_id": booking.resource_id,
            "start_time": booking.start_time,
            "end_time": booking.end_time,
            "status": booking.status,
            "can_review": can_review,
            "has_reviewed": has_reviewed,
        }

        return Response(data)    