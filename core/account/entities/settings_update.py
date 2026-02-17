# core/account/entities/settings_update.py

from core.entities.contracts import BaseEntity
from core.account.models import UserSettings


class AccountSettingsUpdateEntity(BaseEntity):
    """
    Entity: core / account.settings.update
    Update current authenticated user's settings
    """

    key = "account.settings.update"
    domain = "core"
    permission = "core.account.settings.update"

    def query(self, *, user, tenant, query: dict) -> dict:
        raise NotImplementedError("Query not supported for this entity.")
    
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
            "message": "Settings updated successfully",
        }
