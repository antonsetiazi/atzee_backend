# setup/management/commands/seed_customers.py

import importlib

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant

from business.customers.models import Customer


class Command(BaseCommand):

    help = "Seed customers per tenant based on vertical"


    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception(
                "seed_customers cannot run in production."
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
                    f"verticals.{vertical}.seeds.customers"
                )

                seed_module = importlib.import_module(
                    module_path
                )

                config = getattr(
                    seed_module,
                    "CUSTOMERS",
                    None
                )

                if config is None:
                    raise AttributeError(
                        "CUSTOMERS not found"
                    )

            except ModuleNotFoundError:

                self.stdout.write(
                    self.style.WARNING(
                        f"No customer seed found for '{vertical}'"
                    )
                )

                continue

            except AttributeError:

                self.stdout.write(
                    self.style.WARNING(
                        f"CUSTOMERS config missing in '{module_path}'"
                    )
                )

                continue


            self.stdout.write(
                f"Seeding customers for {tenant.name}"
            )


            for item in config:

                obj, created = Customer.objects.update_or_create(
                    tenant=tenant,
                    code=item["code"],
                    defaults={
                        "name": item["name"],
                        "phone": item.get("phone"),
                        "email": item.get("email"),
                        "address": item.get("address"),
                        "notes": item.get("notes"),
                    }
                )

                if created:
                    total_created += 1
                    self.stdout.write(
                        f"Created customer: {obj.code}"
                    )

                else:
                    total_updated += 1
                    self.stdout.write(
                        f"Updated customer: {obj.code}"
                    )


        self.stdout.write(
            self.style.SUCCESS(
                f"Customers seeded. "
                f"Created: {total_created}, "
                f"Updated: {total_updated}"
            )
        )