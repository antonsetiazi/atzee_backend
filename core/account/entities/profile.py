# core/account/entities/profile.py

from core.entities.contracts import BaseEntity
from core.users.models import User


class AccountProfileEntity(BaseEntity):
    """
    Entity: core / account.profile
    Return current authenticated user profile
    """

    key = "account.profile"
    domain = "core"
    permission = "core.account.profile.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        u: User = user

        return {
            "id": str(u.id),
            "username": u.username,
            "full_name": u.full_name,
            "email": u.email,
            "phone": getattr(u, "phone", None),
        }
