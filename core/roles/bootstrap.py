# core/roles/bootstrap.py

from core.roles.models import Role
from core.permissions.models import Permission, RolePermission
from core.roles.enums import RoleCode

ADMIN_ROLE_NAME = "Admin"
ADMIN_ACCESS_LEVEL = 1000


def ensure_admin_role(*, tenant):
    """
    Pastikan tenant punya role Admin.
    """
    role, _ = Role.objects.get_or_create(
        tenant=tenant,
        code=RoleCode.ADMIN,
        defaults={
            "name": ADMIN_ROLE_NAME,
            "description": "Tenant administrator",
            "access_level": ADMIN_ACCESS_LEVEL,
        }
    )
    return role


def assign_all_permissions_to_role(*, role):
    """
    Berikan semua permission tenant ke role ini.
    Idempotent.
    """
    permissions = Permission.objects.filter(
        tenant=role.tenant
    )

    created = 0
    for perm in permissions:
        _, was_created = RolePermission.objects.get_or_create(
            role=role,
            permission=perm,
        )
        if was_created:
            created += 1

    return created
