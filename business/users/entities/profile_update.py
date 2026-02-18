# business/users/entities/profile_update.py

from core.entities.contracts import BaseEntity
from business.users.services import update_business_user
from business.users.selectors import get_user_by_core_user


class BusinessUserProfileUpdateEntity(BaseEntity):
    key = "users.profile.update"
    domain = "business"
    permission = "business.users.self.update"

    def query(self, *, user, tenant, query: dict) -> dict:
        business_user = get_user_by_core_user(
            tenant=tenant,
            core_user_id=user.id,
        )

        updated = update_business_user(
            tenant=tenant,
            user_id=business_user.id,
            updated_by=user,
            **(query or {}),
        )

        return {
            "id": str(updated.id),
            "message": "Business profile updated successfully",
        }
