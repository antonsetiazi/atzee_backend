# core/users/auth/methods/password_login.py

from core.users.models import User
from core.tenants.models import Tenant
from shared.api.exceptions import BusinessException


def authenticate_password(email: str, password: str, tenant_code: str):

    try:
        tenant = Tenant.objects.get(code=tenant_code, is_active=True)
    except Tenant.DoesNotExist:
        raise BusinessException(
            message="Tenant tidak valid",
            code="INVALID_TENANT"
        )

    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        raise BusinessException(
            message="Email salah",
            code="INVALID_CREDENTIALS"
        )

    if not user.check_password(password):
        raise BusinessException(
            message="Password salah",
            code="INVALID_CREDENTIALS"
        )

    if not user.is_active:
        raise BusinessException(
            message="User tidak aktif",
            code="USER_INACTIVE"
        )

    if not user.tenant_memberships.filter(
        tenant=tenant,
        is_active=True
    ).exists():
        raise BusinessException(
            message="Akses tenant tidak tersedia",
            code="TENANT_ACCESS_DENIED"
        )

    return user, tenant