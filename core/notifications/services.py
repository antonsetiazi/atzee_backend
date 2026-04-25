# core/notifications/services.py

from django.core.exceptions import ValidationError
from core.notifications.models import Notification
from core.notifications.events import (
    ALL_NOTIFICATION_EVENTS,
    EVENT_META,
)
from core.notifications.providers.in_app import InAppNotificationProvider
from core.notifications.providers.realtime import RealtimeNotificationProvider


class NotificationService:
    provider_map = {
        "in_app": InAppNotificationProvider(),
        "realtime": RealtimeNotificationProvider(),
    }

    @classmethod
    def notify(
        cls,
        *,
        user,
        event,
        title,
        message,
        tenant=None,
        entity_type=None,
        entity_id=None,
        payload=None,
        channels=None,
    ):
        if event not in ALL_NOTIFICATION_EVENTS:
            raise ValidationError(
                f"Unregistered notification event: {event}"
            )

        meta = EVENT_META.get(event, {})
        level = meta.get("level", "info")

        notification = Notification.objects.create(
            user=user,
            tenant=tenant,
            event=event,
            level=level,
            title=title,
            message=message,
            entity_type=entity_type,
            entity_id=entity_id,
            payload=payload or {},
        )

        for channel in channels or ["in_app", "realtime"]:
            provider = cls.provider_map.get(channel)
            if provider:
                provider.send(notification)

        return notification
