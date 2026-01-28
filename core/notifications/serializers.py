from rest_framework import serializers
from core.notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "type",
            "title",
            "message",
            "payload",
            "is_read",
            "created_at",
        ]
