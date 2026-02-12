# core/schedule/shifts/serializers.py

from rest_framework import serializers
from core.schedule.shifts.models import Shift


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = [
            "id",
            "name",
            "start_datetime",
            "end_datetime",
            "participants",
            "rotation_pattern",
            "metadata",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
