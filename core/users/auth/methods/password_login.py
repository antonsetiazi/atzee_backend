# core/users/auth/methods/password_login.py

from core.users.models import User
from core.tenants.models import Tenant


def authenticate_password(email: str, password: str, tenant_code: str):

    try:
        tenant = Tenant.objects.get(code=tenant_code, is_active=True)
    except Tenant.DoesNotExist:
        raise ValueError("Invalid tenant")

    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        raise ValueError("Invalid credentials")

    if not user.check_password(password):
        raise ValueError("Invalid credentials")

    if not user.is_active:
        raise ValueError("User inactive")

    if not user.tenant_memberships.filter(
        tenant=tenant,
        is_active=True
    ).exists():
        raise ValueError("User not member of this tenant")

    return user, tenant