# core/notifications/serializers.py

from rest_framework import serializers
from core.notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="level")
    read = serializers.BooleanField(source="is_read")

    class Meta:
        model = Notification
        fields = [
            "id",
            "title",
            "message",
            "type",
            "read",
            "created_at",
            "event",
            "entity_type",
            "entity_id",
            "payload",
        ]