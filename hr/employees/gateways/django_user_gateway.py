from uuid import UUID
from typing import Optional

from django.core.exceptions import ValidationError

from core.users.models import User
from hr.employees.gateways.user_gateway import (
    UserGateway,
    UserSnapshot,
)


class DjangoUserGateway(UserGateway):
    """
    Django ORM based implementation for Core User.
    """

    def get_user(self, *, user_id: UUID) -> Optional[UserSnapshot]:
        try:
            user = User.objects.only(
                "id", "email", "is_active"
            ).get(id=user_id)
        except User.DoesNotExist:
            return None
        
        return UserSnapshot(
            id=user.id,
            email=user.email,
            is_active=user.is_active,
        )
    

    def ensure_user_is_active(self, *, user_id: UUID) -> None:
        user = self.get_user(user_id=user_id)

        if not user:
            raise ValidationError(
                "User does not exist."
            )
        
        if not user.is_active:
            raise ValidationError(
                "User is not active."
            )