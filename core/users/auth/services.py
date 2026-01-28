from rest_framework_simplejwt.tokens import RefreshToken


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
