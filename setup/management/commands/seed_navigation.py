# setup/management/commands/seed_navigation.py

from importlib import import_module
from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from core.ui.models import (
    UIMenu,
    TenantNavigationConfig,
    TenantNavigationItem,
)


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

        for tenant in tenants:
            vertical = tenant.vertical

            # coba import vertical-specific navigation
            try:
                nav_module = import_module(f"verticals.{vertical}.seeds.navigation")
                NAVIGATION_SEED = getattr(nav_module, "NAVIGATION_SEED", [])
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(f"No navigation seed found for vertical '{vertical}'")
                )
                continue
            
            for seed in NAVIGATION_SEED:
                tenant_code = seed.get("tenant_code")
                role = seed.get("role")
                nav_type = seed.get("type")
                device = seed.get("device", "all")
                app = seed.get("app")

                # jika tenant_code diset, cocokkan dulu
                if tenant_code and tenant_code != tenant.code:
                    continue

                config, _ = TenantNavigationConfig.objects.update_or_create(
                    tenant=tenant,
                    type=nav_type,
                    device=device,
                    role=role,
                    app=app,
                    defaults={"is_active": True, "is_default": False},
                )

                # bersihkan item lama
                config.items.all().delete()

                for order, item in enumerate(seed.get("items", []), start=1):
                    action_type = item["action_type"]
                    target = item["target"]
                    menu_obj = menus.get(target) if action_type == "menu" else None

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
                self.style.SUCCESS(f"[{tenant.code}] navigation seeded for vertical '{vertical}'")
            )

        self.stdout.write(self.style.SUCCESS("All tenant navigations seeded successfully."))
