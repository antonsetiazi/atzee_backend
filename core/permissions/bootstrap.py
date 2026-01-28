from core.permissions.models import Permission
from core.ui.models import UIMenu


def sync_permissions_from_ui(*, tenant):
    """
    Pastikan semua menu punya permission di tenant ini.
    Idempotent.
    """
    created = 0

    for menu in UIMenu.objects.all():
        code = f"{menu.app}.{menu.resource}.{menu.action}"

        _, was_created = Permission.objects.get_or_create(
            tenant=tenant,
            code=code,
            defaults={
                "description": f"Access {menu.label}",
            }
        )

        if was_created:
            created += 1

    return created
