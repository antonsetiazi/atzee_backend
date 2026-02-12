# core/schedule/reminders/serializers.py

from rest_framework import serializers
from core.schedule.reminders.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = [
            "id",
            "event",
            "reminder_time",
            "reminder_type",
            "repeat_interval",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
