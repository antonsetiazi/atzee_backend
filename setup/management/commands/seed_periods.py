# setup/management/commands/seed_periods.py

import importlib

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant

from accounting.models import AccountingPeriod


class Command(BaseCommand):
    help = "Seed accounting periods per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("seed_periods cannot run in production.")

        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(
                self.style.WARNING("No tenants found.")
            )
            return

        total_created = 0
        total_updated = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.periods"

                period_module = importlib.import_module(module_path)

                periods_config = getattr(
                    period_module,
                    "PERIODS",
                    None
                )

                if periods_config is None:
                    raise AttributeError("PERIODS not found")

            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(
                        f"No period seed found for vertical '{vertical}'"
                    )
                )
                continue

            except AttributeError:
                self.stdout.write(
                    self.style.WARNING(
                        f"PERIODS config not found in '{module_path}'"
                    )
                )
                continue

            self.stdout.write(
                f"Seeding periods for {tenant.name} ({vertical})"
            )

            for item in periods_config:

                obj = AccountingPeriod.objects.filter(
                    tenant=tenant,
                    start_date=item["start_date"],
                    end_date=item["end_date"],
                ).first()

                if obj:
                    is_changed = False

                    if obj.name != item["name"]:
                        obj.name = item["name"]
                        is_changed = True

                    if obj.status != item.get("status", "open"):
                        obj.status = item.get("status", "open")
                        is_changed = True

                    if is_changed:
                        obj.is_closed = obj.status == "closed"
                        obj.is_locked = obj.status == "locked"

                        obj.save()

                        total_updated += 1

                        self.stdout.write(
                            f"Updated period: {obj.name}"
                        )

                else:
                    obj = AccountingPeriod.objects.create(
                        tenant=tenant,
                        name=item["name"],
                        start_date=item["start_date"],
                        end_date=item["end_date"],
                        status=item.get("status", "open"),
                        is_closed=item.get("status") == "closed",
                        is_locked=item.get("status") == "locked",
                    )

                    total_created += 1

                    self.stdout.write(
                        f"Created period: {obj.name}"
                    )

        self.stdout.write(
            self.style.SUCCESS(
                f"Periods seeded. "
                f"Created: {total_created}, "
                f"Updated: {total_updated}"
            )
        )