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

from .serializers import CreateHoldBookingSerializer


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