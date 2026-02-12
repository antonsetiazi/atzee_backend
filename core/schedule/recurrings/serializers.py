# core/schedule/recurrings/serializers.py

from rest_framework import serializers
from core.schedule.recurrings.models import Recurring


class RecurringListSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source="event.title", read_only=True)

    class Meta:
        model = Recurring
        fields = [
            "id",
            "event",
            "event_title",
            "frequency",
            "interval",
            "end_date",
        ]


class RecurringDetailSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source="event.title", read_only=True)
    created_by = serializers.CharField(
        source="created_by.full_name",
        read_only=True
    )

    class Meta:
        model = Recurring
        fields = [
            "id",
            "event",
            "event_title",
            "frequency",
            "interval",
            "end_date",
            "created_at",
            "updated_at",
            "created_by",
        ]


class RecurringCreateSerializer(serializers.Serializer):
    event = serializers.IntegerField()
    frequency = serializers.ChoiceField(
        choices=Recurring.FREQUENCY_CHOICES
    )
    interval = serializers.IntegerField(default=1)
    end_date = serializers.DateField(required=False, allow_null=True)

    def validate_interval(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "interval must be greater than 0."
            )
        return value


class RecurringUpdateSerializer(serializers.Serializer):
    frequency = serializers.ChoiceField(
        choices=Recurring.FREQUENCY_CHOICES,
        required=False
    )
    interval = serializers.IntegerField(required=False)
    end_date = serializers.DateField(required=False, allow_null=True)

    def validate_interval(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "interval must be greater than 0."
            )
        return value
