# core/notifications/providers/realtime.py

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from core.notifications.serializers import NotificationSerializer


class RealtimeNotificationProvider:
    def send(self, notification):
        channel_layer = get_channel_layer()

        group_name = f"user_{notification.user_id}"

        payload = NotificationSerializer(notification).data

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "ws.notification",
                "payload": payload,
            },
        )