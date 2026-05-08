# setup/management/commands/seed_taxes.py

import importlib

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant

from accounting.models import Tax


class Command(BaseCommand):

    help = "Seed taxes per tenant based on vertical"


    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception(
                "seed_taxes cannot run in production."
            )

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

                module_path = (
                    f"verticals.{vertical}.seeds.taxes"
                )

                seed_module = importlib.import_module(
                    module_path
                )

                config = getattr(
                    seed_module,
                    "TAXES",
                    None
                )

                if config is None:
                    raise AttributeError(
                        "TAXES not found"
                    )

            except ModuleNotFoundError:

                self.stdout.write(
                    self.style.WARNING(
                        f"No tax seed found for '{vertical}'"
                    )
                )

                continue

            except AttributeError:

                self.stdout.write(
                    self.style.WARNING(
                        f"TAXES config missing in '{module_path}'"
                    )
                )

                continue


            self.stdout.write(
                f"Seeding taxes for {tenant.name}"
            )


            for item in config:

                obj, created = Tax.objects.update_or_create(
                    tenant=tenant,
                    code=item["code"],
                    defaults={
                        "name": item["name"],
                        "tax_type": item["tax_type"],
                        "rate": item["rate"],
                        "is_active": True,
                    }
                )

                if created:
                    total_created += 1
                    self.stdout.write(
                        f"Created tax: {obj.code}"
                    )

                else:
                    total_updated += 1
                    self.stdout.write(
                        f"Updated tax: {obj.code}"
                    )


        self.stdout.write(
            self.style.SUCCESS(
                f"Taxes seeded. "
                f"Created: {total_created}, "
                f"Updated: {total_updated}"
            )
        )