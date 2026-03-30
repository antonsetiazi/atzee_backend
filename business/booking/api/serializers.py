# business/booking/api/serializers.py

from rest_framework import serializers


class CreateHoldBookingSerializer(serializers.Serializer):
    resource_type = serializers.CharField()
    resource_id = serializers.CharField()

    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    meta = serializers.JSONField(required=False)


class BookingActionSerializer(serializers.Serializer):
    booking_id = serializers.UUIDField()