# setup/management/commands/seed_products.py

import importlib

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant
from business.products.models import Product


class Command(BaseCommand):
    help = "Seed products per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("seed_products cannot run in production.")

        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_created = 0
        total_updated = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.products"
                products_module = importlib.import_module(module_path)
                products_config = getattr(products_module, "PRODUCTS", [])
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(
                        f"No products module found for vertical '{vertical}'"
                    )
                )
                continue

            self.stdout.write(
                f"Seeding products for tenant: {tenant.name} ({vertical})"
            )

            for product_data in products_config:
                product, created = Product.objects.update_or_create(
                    tenant=tenant,
                    code=product_data.get("code"),
                    defaults={
                        "name": product_data.get("name"),
                        "product_type": product_data.get("product_type", Product.TYPE_GOOD),
                        "description": product_data.get("description"),
                    }
                )

                if created:
                    total_created += 1
                else:
                    total_updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Products seeded. Created: {total_created}, Updated: {total_updated}"
            )
        )