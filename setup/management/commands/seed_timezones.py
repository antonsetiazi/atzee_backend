# setup/management/commands/seed_timezones.py

from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from core.geo.timezones.seed import seed_timezones


class Command(BaseCommand):
    help = "Seed default Timezone data for all tenants"

    def handle(self, *args, **options):
        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        for tenant in tenants:
            with transaction.atomic():
                seed_timezones(tenant)

            self.stdout.write(
                self.style.SUCCESS(
                    f"✔ Timezones seeded for tenant: {tenant.code or tenant.name}"
                )
            )
