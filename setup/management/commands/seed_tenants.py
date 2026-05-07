# setup/management/commands/seed_tenants.py

from django.conf import settings
from django.core.management.base import BaseCommand
from core.tenants.models import Tenant
from core.tenants.seed_registry import all_tenant_seeds

import importlib


class Command(BaseCommand):
    help = "Seed default tenants"

    def handle(self, *args, **kwargs):

        # 🔥 Load seeds berdasarkan ENV verticals
        for vertical in settings.VERTICALS:
            try:
                importlib.import_module(
                    f"verticals.{vertical}.seeds.tenants"
                )
                self.stdout.write(f"Loaded seeds: {vertical}")
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(
                        f"No tenant seeds for: {vertical}"
                    )
                )

        # 🚀 Jalankan registry
        for data in all_tenant_seeds():
            obj, created = Tenant.objects.update_or_create(
                code=data["code"],
                defaults={
                    "name": data["name"],
                    "vertical": data["vertical"],
                    "is_active": data.get("is_active", True),
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Created tenant: {obj.code}"
                ))
            else:
                self.stdout.write(
                    f"Updated tenant: {obj.code}"
                )
