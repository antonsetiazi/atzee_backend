from core.permissions.bootstrap import sync_permissions_from_ui
from core.roles.bootstrap import (
    ensure_admin_role,
    assign_all_permissions_to_role,
)


def bootstrap_tenant_permissions(*, tenant):
    """
    FULL permission bootstrap untuk tenant.
    Aman dipanggil berkali-kali.
    """

    # 1. sync permissions
    sync_permissions_from_ui(tenant=tenant)

    # 2. ensure admin role
    admin_role = ensure_admin_role(tenant=tenant)

    # 3. assign all permissions to admin
    assign_all_permissions_to_role(role=admin_role)
