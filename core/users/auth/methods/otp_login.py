# core/users/auth/methods/otp_login.py

from core.users.models import User
from core.tenants.models import Tenant, UserTenant
from core.roles.models import UserRole
from core.roles.enums import RoleCode
from core.otp.services import OTPService
from shared.utils.phone import normalize_phone


def authenticate_otp(phone: str, otp: str, tenant_code: str):
    phone = normalize_phone(phone)

    # 1️⃣ Verify OTP
    if not OTPService.verify_otp(phone, otp):
        raise ValueError("Invalid or expired OTP")

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
        raise ValueError("Invalid tenant")

    # 4️⃣ Ensure tenant membership
    membership, _ = UserTenant.objects.get_or_create(
        user=user,
        tenant=tenant,
        defaults={
            "is_active": True
        }
    )

    
    # Check membership
    membership = user.tenant_memberships.filter(
        tenant=tenant
    ).first()

    if not membership:
        # raise ValueError("User does not belong to this tenant")
        UserRole.objects.get_or_create(
            user=user,
            role=RoleCode.CUSTOMER
        )

    return user, tenant