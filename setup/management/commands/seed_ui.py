# setup/management/commands/seed_ui.py

from django.core.management.base import BaseCommand
from shared.ui.bootstrap import seed_ui

from core.ui.seed_menus import UI_MENUS as CORE_MENUS
from core.ui.seed_pages import UI_PAGES as CORE_PAGES

from business.ui.seed_menus import UI_MENUS as BUSINESS_MENUS
from business.ui.seed_pages import UI_PAGES as BUSINESS_PAGES

from accounting.ui.seed_menus import UI_MENUS as ACCOUNTING_MENUS
from accounting.ui.seed_pages import UI_PAGES as ACCOUNTING_PAGES

from hr.ui.seed_menus import UI_MENUS as HR_MENUS
from hr.ui.seed_pages import UI_PAGES as HR_PAGES

# Permission
from core.permissions.registry import PermissionRegistry
from core.permissions.models import Permission
from core.tenants.models import Tenant
from core.ui.schema.page import Page
from core.ui.schema.serialize import page_to_dict


def register_permissions_from_pages(pages: list[dict]):
    """
    Ambil semua permissions dari pages & actions lalu register ke PermissionRegistry
    """
    for page in pages:
        # 🔹 jika page adalah typed Page, convert dulu ke dict
        if isinstance(page, Page):
            page = page_to_dict(page)

        # page-level permissions
        for code in page.get("permissions", []):
            PermissionRegistry.register([{
                "code": code,
                "description": f"Permission for entity '{page['key']}'"
            }])

        # loop semua blocks
        for block in page.get("blocks", []):
            # actions di block
            for action in block.get("actions", []):
                if action.get("permission"):
                    PermissionRegistry.register([{
                        "code": action["permission"],
                        "description": f"Action '{action['label']}' in '{page['key']}'"
                    }])
            # top_actions
            for action in block.get("top_actions", []):
                if action.get("permission"):
                    PermissionRegistry.register([{
                        "code": action["permission"],
                        "description": f"Top action '{action['label']}' in '{page['key']}'"
                    }])


def sync_permissions_to_db():
    """
    Ambil semua permissions yang sudah ter-registrasi di PermissionRegistry
    lalu simpan ke database untuk semua tenant
    """
    for tenant in Tenant.objects.all():
        for perm in PermissionRegistry.all():
            obj, created = Permission.objects.get_or_create(
                tenant=tenant,
                code=perm["code"],
                defaults={
                    "description": perm.get("description", "")
                }
            )
            if created:
                print(f"[{tenant}] Created permission: {perm['code']}")
            else:
                print(f"[{tenant}] Permission exists: {perm['code']}")


class Command(BaseCommand):
    help = "Seed UI schema (menus & pages) + sync all permissions automatically"

    def handle(self, *args, **options):
        modules = [
            (CORE_MENUS, CORE_PAGES),
            (BUSINESS_MENUS, BUSINESS_PAGES),
            (ACCOUNTING_MENUS, ACCOUNTING_PAGES),
            (HR_MENUS, HR_PAGES),
        ]

        for menus, pages in modules:
            # print("===================================================")
            # print(pages)
            # 1️⃣ Seed UI schema
            seed_ui(menus=menus, pages=pages)

            # 2️⃣ Register permissions dari pages & actions
            register_permissions_from_pages(pages)

        # 3️⃣ Sync permissions ke database
        sync_permissions_to_db()

        self.stdout.write(self.style.SUCCESS("All UI schema seeded and permissions synced successfully"))
