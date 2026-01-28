from django.db import transaction
from core.roles.models import Role, UserRole
from core.roles.bootstrap import ADMIN_ROLE_NAME

def list_roles(*, tenant):
    return Role.objects.filter(tenant=tenant)


@transaction.atomic
def create_role(*, tenant, data):
    return Role.objects.create(
        tenant=tenant,
        name=data["name"],
        description=data.get("description", ""),
        access_level=data["access_level"],
    )


@transaction.atomic
def update_role(*, tenant, role_id, data):
    role = Role.objects.get(
        id=role_id,
        tenant=tenant
    )

    for field in ["name", "description", "access_level"]:
        if field in data:
            setattr(role, field, data[field])

    role.save()
    return role


def ensure_user_has_role(*, user, tenant):
    """
    Pastikan user punya minimal satu role di tenant ini.
    Dipanggil saat user switch / masuk tenant.
    """

    exists = UserRole.objects.filter(
        user=user,
        role__tenant=tenant,
    ).exists()

    if exists:
        return  # sudah aman

    # ambil role default (access_level terendah)
    default_role = Role.objects.filter(
        tenant=tenant
    ).order_by("access_level").first()

    if not default_role:
        raise Exception("Tenant has no roles defined")

    UserRole.objects.create(
        user=user,
        role=default_role,
    )


def ensure_user_is_admin(*, user, tenant):
    """
    Pastikan user punya admin role (kalau belum punya role apapun).
    """
    has_role = UserRole.objects.filter(
        user=user,
        role__tenant=tenant,
    ).exists()

    if has_role:
        return

    admin_role = Role.objects.get(
        tenant=tenant,
        name=ADMIN_ROLE_NAME,
    )

    UserRole.objects.create(
        user=user,
        role=admin_role,
    )