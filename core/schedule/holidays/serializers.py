# core/schedule/holidays/serializers.py

from rest_framework import serializers
from core.schedule.holidays.models import Holiday


class HolidaySerializer(serializers.ModelSerializer):
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
        read_only_fields = ["id", "created_at", "updated_at"]
