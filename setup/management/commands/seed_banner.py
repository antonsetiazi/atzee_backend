# setup/management/commands/seed_banner.py

import importlib

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant
from core.widgets.models import UIWidget


class Command(BaseCommand):
    help = "Seed banners per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("seed_banner cannot run in production.")

        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_created = 0
        total_updated = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.banners"
                banners_module = importlib.import_module(module_path)
                banners_config = getattr(banners_module, "BANNERS", [])
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(
                        f"No banners module found for vertical '{vertical}'"
                    )
                )
                continue

            self.stdout.write(
                f"Seeding banners for tenant: {tenant.name} ({vertical})"
            )

            for banner in banners_config:
                widget, created = UIWidget.objects.update_or_create(
                    tenant=tenant,
                    type="banner",
                    position=banner["position"],
                    title=banner.get("title"),
                    defaults={
                        "config": banner.get("config", {}),
                        "starts_at": banner.get("starts_at"),
                        "ends_at": banner.get("ends_at"),
                        "target_roles": banner.get("target_roles", []),
                        "target_permissions": banner.get("target_permissions", []),
                        "order": banner.get("order", 50),
                        "is_active": banner.get("is_active", True),
                    }
                )

                if created:
                    total_created += 1
                else:
                    total_updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Banners seeded. Created: {total_created}, Updated: {total_updated}"
        ))
