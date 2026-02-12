# core/schedule/reminders/serializers.py

from rest_framework import serializers
from core.schedule.reminders.models import Reminder


class ReminderListSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source="event.title", read_only=True)

    class Meta:
        model = Reminder
        fields = [
            "id",
            "event",
            "event_title",
            "reminder_time",
            "reminder_type",
        ]


class ReminderDetailSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source="event.title", read_only=True)
    created_by = serializers.CharField(source="created_by.full_name", read_only=True)

    class Meta:
        model = Reminder
        fields = [
            "id",
            "event",
            "event_title",
            "reminder_time",
            "reminder_type",
            "repeat_interval",
            "created_at",
            "updated_at",
            "created_by",
        ]


class ReminderCreateSerializer(serializers.Serializer):
    event = serializers.IntegerField()
    reminder_time = serializers.DurationField()
    reminder_type = serializers.ChoiceField(
        choices=Reminder.REMINDER_TYPE_CHOICES
    )
    repeat_interval = serializers.DurationField(required=False, allow_null=True)

    def validate_reminder_time(self, value):
        if value.total_seconds() <= 0:
            raise serializers.ValidationError(
                "reminder_time must be greater than 0."
            )
        return value


class ReminderUpdateSerializer(serializers.Serializer):
    reminder_time = serializers.DurationField(required=False)
    reminder_type = serializers.ChoiceField(
        choices=Reminder.REMINDER_TYPE_CHOICES,
        required=False
    )
    repeat_interval = serializers.DurationField(required=False, allow_null=True)

    def validate_reminder_time(self, value):
        if value.total_seconds() <= 0:
            raise serializers.ValidationError(
                "reminder_time must be greater than 0."
            )
        return value
