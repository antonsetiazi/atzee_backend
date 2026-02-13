# setup/management/commands/seed_navigation.py

from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from core.ui.models import (
    UIMenu,
    TenantNavigationConfig,
    TenantNavigationItem,
)
from core.ui.seed_navigations import NAVIGATION_SEED


class Command(BaseCommand):
    help = "Seed tenant-specific navigation strategy (sidebar, bottom, drawer)"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Seeding tenant navigation strategy...")

        tenants = Tenant.objects.filter(is_active=True)

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No active tenants found."))
            return

        # Optional: preload menus for backward compatibility
        menus = {m.key: m for m in UIMenu.objects.all()}

        for seed in NAVIGATION_SEED:
            tenant_code = seed.get("tenant_code")
            role = seed.get("role")
            nav_type = seed.get("type")
            device = seed.get("device", "all")
            app = seed.get("app")

            applicable_tenants = tenants
            if tenant_code:
                applicable_tenants = tenants.filter(code=tenant_code)

            for tenant in applicable_tenants:
                config, _ = TenantNavigationConfig.objects.update_or_create(
                    tenant=tenant,
                    type=nav_type,
                    device=device,
                    role=role,
                    app=app,
                    defaults={
                        "is_active": True,
                        "is_default": False,
                    },
                )

                # Clear old items (idempotent seeding)
                config.items.all().delete()

                for order, item in enumerate(seed.get("items", []), start=1):
                    action_type = item["action_type"]
                    target = item["target"]

                    # Backward compatibility:
                    # If action_type == "menu", try resolve UIMenu
                    menu_obj = None
                    if action_type == "menu":
                        menu_obj = menus.get(target)

                    TenantNavigationItem.objects.create(
                        navigation=config,
                        menu=menu_obj,
                        action_type=action_type,
                        target=target,
                        label_override=item.get("label"),
                        icon_override=item.get("icon"),
                        route_override=item.get("route"),
                        is_primary=item.get("is_primary", False),
                        badge_source=item.get("badge_source"),
                        order=order,
                        is_active=True,
                    )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"[{tenant.code}] {nav_type} ({device}) → role={role}, app={app}"
                    )
                )

        self.stdout.write(self.style.SUCCESS("Tenant navigation strategy seeding done."))
