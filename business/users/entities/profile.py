# business/users/entities/profile.py

from core.entities.contracts import BaseEntity
from business.users.selectors import get_user_by_core_user


class BusinessUserProfileEntity(BaseEntity):
    key = "users.profile"
    domain = "business"
    permission = "business.users.self.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        business_user = get_user_by_core_user(
            tenant=tenant,
            core_user_id=user.id,
        )

        if not business_user:
            return {}

        return {
            "id": str(business_user.id),
            "name": business_user.name,
            "email": business_user.email,
            "phone": business_user.phone,
            "organization_name": business_user.organization_name,
            "organization_type": business_user.organization_type,
            "address": business_user.address,
            "latitude": business_user.latitude,
            "longitude": business_user.longitude,
            "notes": business_user.notes,
        }
