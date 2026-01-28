class BaseNotificationProvider:
    def send(self, notification):
        raise NotImplementedError("Provider must implement send()")
