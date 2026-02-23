# setup/management/commands/seed_partners.py

import importlib
import random

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant
from business.partners.models import Partner
from business.products.models import Product, PartnerProduct


class Command(BaseCommand):
    help = "Seed partners + products per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("seed_partners cannot run in production.")

        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_partner_created = 0
        total_partner_updated = 0
        total_product_created = 0
        total_partner_product_created = 0

        for tenant in tenants:
            vertical = tenant.vertical

            self.stdout.write(
                self.style.MIGRATE_HEADING(
                    f"\nSeeding tenant: {tenant.name} ({vertical})"
                )
            )

            # ─────────────────────────────────────────────
            # LOAD PARTNER CONFIG
            # ─────────────────────────────────────────────
            try:
                partner_module_path = f"verticals.{vertical}.seeds.partners"
                partner_module = importlib.import_module(partner_module_path)
                partners_config = getattr(partner_module, "PARTNERS", [])
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(
                        f"No partners module found for vertical '{vertical}'"
                    )
                )
                continue

            # ─────────────────────────────────────────────
            # LOAD PRODUCT CONFIG
            # ─────────────────────────────────────────────
            try:
                product_module_path = f"verticals.{vertical}.seeds.products"
                product_module = importlib.import_module(product_module_path)
                products_config = getattr(product_module, "PRODUCTS", [])
            except ModuleNotFoundError:
                products_config = []
                self.stdout.write(
                    self.style.WARNING(
                        f"No products module found for vertical '{vertical}'"
                    )
                )

            # ─────────────────────────────────────────────
            # SEED PRODUCTS
            # ─────────────────────────────────────────────
            tenant_products = []

            for pdata in products_config:
                product, created = Product.objects.update_or_create(
                    tenant=tenant,
                    code=pdata.get("code"),
                    defaults={
                        "name": pdata["name"],
                        "product_type": pdata.get("product_type", Product.TYPE_SERVICE),
                        "description": pdata.get("description"),
                    },
                )

                tenant_products.append(product)

                if created:
                    total_product_created += 1

            # ─────────────────────────────────────────────
            # SEED PARTNERS
            # ─────────────────────────────────────────────
            for data in partners_config:
                partner, created = Partner.objects.update_or_create(
                    tenant=tenant,
                    code=data.get("code"),
                    defaults={
                        "name": data["name"],
                        "email": data.get("email"),
                        "phone": data.get("phone"),
                        "address": data.get("address"),
                        "notes": data.get("notes"),
                        "search_latitude": data.get("latitude"),
                        "search_longitude": data.get("longitude"),
                        "base_price": data.get("base_price"),
                        "rating_avg": data.get("rating_avg", 0),
                        "rating_count": data.get("rating_count", 0),
                    },
                )

                if created:
                    total_partner_created += 1
                else:
                    total_partner_updated += 1

                # ─────────────────────────────────────────
                # ASSIGN 3 RANDOM PRODUCTS PER PARTNER
                # ─────────────────────────────────────────
                if tenant_products:
                    selected_products = random.sample(
                        tenant_products,
                        min(3, len(tenant_products))
                    )

                    for product in selected_products:
                        _, pp_created = PartnerProduct.objects.update_or_create(
                            tenant=tenant,
                            partner=partner,
                            product=product,
                            defaults={
                                "price": (
                                    (partner.base_price or 200000)
                                    + random.randint(-50000, 50000)
                                ),
                                "duration_minutes": random.choice([60, 90, 120]),
                                "is_active": True,
                            },
                        )

                        if pp_created:
                            total_partner_product_created += 1

        # ─────────────────────────────────────────────
        # SUMMARY
        # ─────────────────────────────────────────────
        self.stdout.write(
            self.style.SUCCESS(
                "\nSeeding completed:\n"
                f"Partners Created: {total_partner_created}\n"
                f"Partners Updated: {total_partner_updated}\n"
                f"Products Created: {total_product_created}\n"
                f"PartnerProducts Created: {total_partner_product_created}"
            )
        )