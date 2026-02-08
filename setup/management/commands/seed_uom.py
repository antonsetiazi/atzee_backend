# core/setup/management/commands/seed_uom.py

from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from core.master.uom.seed import seed_uom_categories


class Command(BaseCommand):
    help = "Seed default Unit of Measure data for all tenants"

    def handle(self, *args, **options):
        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        for tenant in tenants:
            with transaction.atomic():
                seed_uom_categories(tenant)

            self.stdout.write(
                self.style.SUCCESS(
                    f"✔ UOM seeded for tenant: {tenant.code or tenant.name}"
                )
            )
