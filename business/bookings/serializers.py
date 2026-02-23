# business/bookings/serializers.py

from rest_framework import serializers
from business.bookings.models import Booking, BookingItem


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


class BookingItemInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)
    unit_price = serializers.DecimalField(max_digits=12, decimal_places=2)
    subtotal = serializers.DecimalField(max_digits=12, decimal_places=2)

class BookingCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    partner_id = serializers.IntegerField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    items = BookingItemInputSerializer(many=True)
    
    location_address = serializers.CharField(required=False)
    location_lat = serializers.DecimalField(max_digits=10, decimal_places=7, required=False)
    location_lng = serializers.DecimalField(max_digits=10, decimal_places=7, required=False)


class BookingItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = BookingItem
        fields = [
            "id",
            "product_name",
            "quantity",
            "unit_price",
            "subtotal",
        ]


class BookingDetailSerializer(serializers.ModelSerializer):
    items = BookingItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            "id",
            "booking_number",
            "start_time",
            "end_time",
            "duration_minutes",
            "subtotal_amount",
            "platform_fee",
            "total_price",
            "status",
            "payment_status",
            "location_address",
            "location_lat",
            "location_lng",
            "items",
        ]