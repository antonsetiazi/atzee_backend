# setup/management/commands/seed_ui.py

from django.core.management.base import BaseCommand
from shared.ui.bootstrap import seed_ui

# Permission
from core.permissions.registry import PermissionRegistry
from core.permissions.models import Permission
from core.tenants.models import Tenant
from core.ui.schema.page import Page
from core.ui.schema.serialize import page_to_dict

from core.ui.registry import UI_MODULE_MENUS, UI_MODULE_PAGES


def register_permissions_from_pages(pages: list[dict]):
    """
    Ambil semua permissions dari pages & actions lalu register ke PermissionRegistry
    """
    for page in pages:
        # 🔹 jika page adalah typed Page, convert dulu ke dict
        # print(page)
        if isinstance(page, Page):
            page = page_to_dict(page)

        module = page["domain"]

        # print(module)

        # page-level permissions
        for code in page.get("permissions", []):
            PermissionRegistry.register([{
                "module": module,
                "code": code,
                "description": f"Permission for entity '{page['key']}'"
            }])

        # loop semua blocks
        for block in page.get("blocks", []):
            # 🔥 block-level permissions
            for code in block.get("permissions", []):
                PermissionRegistry.register([{
                    "module": module,
                    "code": code,
                    "description": f"Block permission in '{page['key']}'"
                }])

            # actions di block
            for action in block.get("actions", []):
                if action.get("permission"):
                    PermissionRegistry.register([{
                        "module": module,
                        "code": action["permission"],
                        "description": f"Action '{action['label']}' in '{page['key']}'"
                    }])
            # top_actions
            for action in block.get("top_actions", []):
                if action.get("permission"):
                    PermissionRegistry.register([{
                        "module": module,
                        "code": action["permission"],
                        "description": f"Top action '{action['label']}' in '{page['key']}'"
                    }])


def sync_permissions_to_db():
    """
    Ambil semua permissions yang sudah ter-registrasi di PermissionRegistry
    lalu simpan ke database untuk semua tenant
    """
    for tenant in Tenant.objects.all():
        tenant_vertical = tenant.vertical

        for perm in PermissionRegistry.all():
            perm_module = perm.get("module")
            
            # 🔥 FILTER DOMAIN
            if perm_module not in ["core", "business", "marketplace", tenant_vertical]:
                continue

            obj, created = Permission.objects.get_or_create(
                tenant=tenant,
                code=perm["code"],
                defaults={
                    "description": perm.get("description", ""),
                    "module": perm.get("module"),
                }
            )
            if created:
                print(f"[{tenant}] Created permission: {perm['code']}")
            else:
                print(f"[{tenant}] Permission exists: {perm['code']}")


class Command(BaseCommand):
    help = "Seed UI schema (menus & pages) + sync all permissions automatically"

    def handle(self, *args, **options):
        modules = set(UI_MODULE_MENUS.keys()) | set(UI_MODULE_PAGES.keys())

        # for menus, pages in modules:
        for module in modules:
            menus = UI_MODULE_MENUS.get(module, [])
            pages = UI_MODULE_PAGES.get(module, [])
            # print("===================================================")
            # print(pages)
            # 1️⃣ Seed UI schema
            seed_ui(menus=menus, pages=pages)

            # 2️⃣ Register permissions dari pages & actions
            register_permissions_from_pages(pages)

        # 3️⃣ Sync permissions ke database
        sync_permissions_to_db()

        self.stdout.write(self.style.SUCCESS("All UI schema seeded and permissions synced successfully"))
