# core/realtime/services.py

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_user_event(user_id: int, payload: dict):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",
        {
            "type": "push_event",
            "data": payload
        }
    )