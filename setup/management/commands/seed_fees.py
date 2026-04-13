# setup/management/commands/seed_fees.py

import importlib
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant
from core.fees.models import FeeConfig


class Command(BaseCommand):
    help = "Seed fees per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise Exception("seed_fees cannot run in production.")

        tenants = Tenant.objects.all()
        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_created = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.fees"
                fees_module = importlib.import_module(module_path)

                fees_config = getattr(fees_module, "FEES", None)
                if fees_config is None:
                    raise AttributeError("FEES not found")

            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(f"No fees module found for vertical '{vertical}'")
                )
                continue

            except AttributeError:
                self.stdout.write(
                    self.style.WARNING(f"FEES config not found in module '{module_path}'")
                )
                continue

            # =========================
            # CLEAR EXISTING (OPTIONAL)
            # =========================
            FeeConfig.objects.filter(tenant=tenant).delete()

            # =========================
            # CREATE NEW
            # =========================
            for fee_data in fees_config:
                FeeConfig.objects.create(
                    tenant=tenant,
                    name=fee_data["name"],
                    fee_type=fee_data["fee_type"],
                    value=fee_data["value"],
                    applies_to=fee_data["applies_to"],
                )
                total_created += 1

            self.stdout.write(
                f"Fees seeded for tenant {tenant.name} ({vertical})"
            )

        self.stdout.write(
            self.style.SUCCESS(f"Fees seeded successfully. Total created: {total_created}")
        )