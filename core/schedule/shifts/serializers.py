# core/schedule/shifts/serializers.py

from rest_framework import serializers
from core.schedule.shifts.models import Shift
from core.users.models import User


# =========================
# LIST
# =========================

class ShiftListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = [
            "id",
            "name",
            "start_datetime",
            "end_datetime",
        ]


# =========================
# DETAIL
# =========================

class ShiftDetailSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Shift
        fields = [
            "id",
            "name",
            "start_datetime",
            "end_datetime",
            "participants",
            "metadata",
            "created_at",
            "updated_at",
        ]


# =========================
# CREATE
# =========================

class ShiftCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        required=False,
    )
    metadata = serializers.JSONField(required=False)


# =========================
# UPDATE
# =========================

class ShiftUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    start_datetime = serializers.DateTimeField(required=False)
    end_datetime = serializers.DateTimeField(required=False)
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        required=False,
    )
    metadata = serializers.JSONField(required=False)

