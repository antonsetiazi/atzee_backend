# setup/management/commands/seed_transaction_types.py

from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from business.transactions.seed.transaction_types import (
    seed_transaction_types
)


class Command(BaseCommand):
    help = "Seed default Transaction Types for all tenants"

    def handle(self, *args, **options):
        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        for tenant in tenants:
            with transaction.atomic():
                seed_transaction_types(tenant)

            self.stdout.write(
                self.style.SUCCESS(
                    f"✔ Transaction Types seeded for tenant: {tenant.code or tenant.name}"
                )
            )