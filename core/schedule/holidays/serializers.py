# core/schedule/holidays/serializers.py

from rest_framework import serializers
from core.schedule.holidays.models import Holiday


class HolidayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = [
            "id",
            "name",
            "start_datetime",
            "end_datetime",
            "all_day",
            "recurring",
        ]


class HolidayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = [
            "id",
            "name",
            "start_datetime",
            "end_datetime",
            "all_day",
            "recurring",
            "metadata",
            "created_at",
            "updated_at",
        ]


class HolidayCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    all_day = serializers.BooleanField(required=False, default=True)
    recurring = serializers.BooleanField(required=False, default=False)
    metadata = serializers.JSONField(required=False)


class HolidayUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    start_datetime = serializers.DateTimeField(required=False)
    end_datetime = serializers.DateTimeField(required=False)
    all_day = serializers.BooleanField(required=False)
    recurring = serializers.BooleanField(required=False)
    metadata = serializers.JSONField(required=False)

