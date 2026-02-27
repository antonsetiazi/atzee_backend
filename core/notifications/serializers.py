# core/notifications/serializers.py

from rest_framework import serializers
from core.notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "event",
            "level",
            "title",
            "message",
            "entity_type",
            "entity_id",
            "payload",
            "is_read",
            "created_at",
        ]