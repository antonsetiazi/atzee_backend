# core/permissions/bootstrap.py

from core.permissions.models import Permission
from core.ui.models import UIMenu


def sync_permissions_from_ui(*, tenant):
    """
    Pastikan semua menu punya permission di tenant ini.
    Idempotent.
    """
    created = 0
    tenant_vertical = tenant.vertical

    for menu in UIMenu.objects.all():
        module = menu.app  # atau mapping lain kalau perlu
        code = f"{menu.app}.{menu.resource}.{menu.action}"

        # 🔥 FILTER
        if module != "core" and module != tenant_vertical:
            continue

        _, was_created = Permission.objects.get_or_create(
            tenant=tenant,
            code=code,
            defaults={
                "description": f"Access {menu.label}",
                "module": module,
            }
        )

        if was_created:
            created += 1

    return created
