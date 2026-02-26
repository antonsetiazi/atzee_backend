# setup/management/commands/seed_branding.py

import importlib
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant

class Command(BaseCommand):
    help = "Seed branding per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise Exception("seed_branding cannot run in production.")

        tenants = Tenant.objects.all()
        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_updated = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.branding"
                branding_module = importlib.import_module(module_path)
                branding_config = getattr(branding_module, "BRANDING", None)
                if branding_config is None:
                    raise AttributeError("BRANDING not found")
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(f"No branding module found for vertical '{vertical}'")
                )
                continue
            except AttributeError:
                self.stdout.write(
                    self.style.WARNING(f"BRANDING config not found in module '{module_path}'")
                )
                continue

            tenant.branding = branding_config
            tenant.save(update_fields=["branding"])
            total_updated += 1
            self.stdout.write(f"Branding updated for tenant {tenant.name} ({vertical})")

        self.stdout.write(self.style.SUCCESS(f"Branding seeded. Total tenants updated: {total_updated}"))