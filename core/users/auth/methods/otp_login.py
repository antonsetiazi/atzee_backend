# core/users/auth/methods/otp_login.py

from core.users.models import User
from core.tenants.models import Tenant, UserTenant
from core.roles.models import Role
from core.roles.models import UserRole
from core.roles.enums import RoleCode
from core.otp.services import OTPService
from shared.utils.phone import normalize_phone
from shared.api.exceptions import BusinessException


def authenticate_otp(phone: str, otp: str, tenant_code: str):
    phone = normalize_phone(phone)

    # 1️⃣ Verify OTP
    if not OTPService.verify_otp(phone, otp):
        raise BusinessException(
            message="OTP tidak valid atau sudah expired",
            code="INVALID_OTP"
        )

    # 2️⃣ Get or create user (phone-first identity)
    user, created = User.objects.get_or_create(
        phone=phone,
        defaults={
            "username": phone,
            "is_active": True,
        }
    )

    # Mark phone verified
    if not user.is_phone_verified:
        user.is_phone_verified = True
        user.save(update_fields=["is_phone_verified"])

    # 3️⃣ Get tenant
    try:
        tenant = Tenant.objects.get(
            code=tenant_code, 
            is_active=True
        )
    except Tenant.DoesNotExist:
        raise BusinessException(
            message="Tenant tidak valid",
            code="INVALID_TENANT"
        )

    # 4️⃣ Ensure tenant membership
    UserTenant.objects.get_or_create(
        user=user,
        tenant=tenant,
        defaults={
            "is_active": True
        }
    )

    role = Role.objects.filter(
        code=RoleCode.CUSTOMER,
        tenant=tenant
    ).first()

    if not role:
        raise ValueError("Default CUSTOMER role not configured for this tenant")

    UserRole.objects.get_or_create(
        user=user,
        role=role
    )

    return user, tenant