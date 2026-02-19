# business/bookings/serializers.py

from rest_framework import serializers
from business.bookings.models import Booking


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "booking_number",
            "user",
            "partner",
            "start_time",
            "status",
            "total_price",
        ]


class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class BookingCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    partner_id = serializers.IntegerField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    location_address = serializers.CharField(required=False)
    location_lat = serializers.DecimalField(max_digits=10, decimal_places=7, required=False)
    location_lng = serializers.DecimalField(max_digits=10, decimal_places=7, required=False)
