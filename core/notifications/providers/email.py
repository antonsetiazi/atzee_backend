from .base import BaseNotificationProvider


class EmailNotificationProvider(BaseNotificationProvider):
    def send(self, notification):
        # TODO: integrate email service
        return True
