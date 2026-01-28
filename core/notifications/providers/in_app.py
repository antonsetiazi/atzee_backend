from .base import BaseNotificationProvider


class InAppNotificationProvider(BaseNotificationProvider):
    def send(self, notification):
        # In-app already persisted in DB
        return True
