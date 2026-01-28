from core.notifications.models import Notification
from core.notifications.providers.in_app import InAppNotificationProvider


class NotificationService:
    provider_map = {
        "in_app": InAppNotificationProvider(),
    }

    @classmethod
    def notify(
        cls,
        *,
        user,
        title,
        message,
        tenant=None,
        payload=None,
        notif_type="info",
        channels=None
    ):
        """
        channels: ["in_app", "email", ...]
        """

        notification = Notification.objects.create(
            user=user,
            tenant=tenant,
            title=title,
            message=message,
            payload=payload or {},
            type=notif_type,
        )

        for channel in channels or ["in_app"]:
            provider = cls.provider_map.get(channel)
            if provider:
                provider.send(notification)

        return notification
