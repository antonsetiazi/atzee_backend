# core/schedule/recurring/serializers.py

from rest_framework import serializers
from core.schedule.recurring.models import RecurringRule


class RecurringRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringRule
        fields = [
            "id",
            "event",
            "rrule",
            "end_date",
            "exceptions",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
