# core/users/auth/services.py

from rest_framework_simplejwt.tokens import RefreshToken
from core.users.models import User


class AuthTokenService:
    """
    Centralized JWT issuing service for Core Platform.
    """

    @staticmethod
    def issue_tokens(user, *, active_tenant_id: str):
        refresh = RefreshToken.for_user(user)

        # CORE CLAIMS (LOCKED)
        refresh["active_tenant"] = str(active_tenant_id)
        refresh["user_id"] = str(user.id)
        refresh["username"] = user.username

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }


# === BACKWARD / PUBLIC CONTRACT ===
def issue_jwt_for_user(user, active_tenant_id: str):
    """
    Public helper used by other core modules (tenant, login, refresh).
    Do NOT put logic here.
    """
    return AuthTokenService.issue_tokens(
        user=user,
        active_tenant_id=active_tenant_id,
    )


def update_user_profile(*, user: User, data: dict) -> User:
    allowed_fields = ["full_name", "phone"]

    updated_fields = []

    for field in allowed_fields:
        if field in data:
            setattr(user, field, data[field])
            updated_fields.append(field)

    if updated_fields:
        user.full_clean()  # validasi model
        user.save(update_fields=updated_fields)

    return user


def change_user_password(user: User, new_password: str) -> User:
    """
    Change user's password safely
    """
    user.set_password(new_password)
    user.full_clean()
    user.save(update_fields=["password"])
    return user