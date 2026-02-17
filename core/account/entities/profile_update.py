# core/account/entities/profile_update.py

from core.entities.contracts import BaseEntity
from core.users.auth.services import update_user_profile


class AccountProfileUpdateEntity(BaseEntity):
    """
    Entity: core / account.profile.update
    Update current authenticated user profile
    """

    key = "account.profile.update"
    domain = "core"
    permission = "core.account.profile.update"

    def query(self, *, user, tenant, query: dict) -> dict:
        updated_user = update_user_profile(
            user=user,
            data=query or {},
        )

        return {
            "id": str(updated_user.id),
            "message": "Profile updated successfully",
        }
