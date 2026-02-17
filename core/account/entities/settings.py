# core/account/entities/settings.py

from core.entities.contracts import BaseEntity
from core.account.models import UserSettings


class AccountSettingsEntity(BaseEntity):
    """
    Entity: core / account.settings
    Manage current authenticated user's settings
    """

    key = "account.settings"
    domain = "core"
    permission = "core.account.settings.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        settings, _ = UserSettings.objects.get_or_create(user=user)

        return {
            "language": settings.language,
            "timezone": settings.timezone,
            "theme": settings.theme,
            "email_notifications": settings.email_notifications,
        }

    def execute(self, *, user, tenant, data: dict) -> dict:
        settings, _ = UserSettings.objects.get_or_create(user=user)

        settings.language = data.get("language", settings.language)
        settings.timezone = data.get("timezone", settings.timezone)
        settings.theme = data.get("theme", settings.theme)
        settings.email_notifications = data.get(
            "email_notifications",
            settings.email_notifications,
        )

        settings.save()

        return {
            "detail": "Settings updated successfully"
        }
