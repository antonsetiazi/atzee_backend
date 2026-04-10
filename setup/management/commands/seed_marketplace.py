# setup/management/commands/seed_marketplace.py

import importlib

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant
from business.partners.models import Partner
from marketplace.models.catalog import MarketplaceProduct
from marketplace.models.listing import PartnerListing
from core.classifications.categories.models import Category


class Command(BaseCommand):
    help = "Seed marketplace products & listings"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("seed_marketplace cannot run in production.")

        tenants = Tenant.objects.all()

        total_product_created = 0
        total_listing_created = 0

        for tenant in tenants:
            vertical = tenant.vertical

            self.stdout.write(
                self.style.MIGRATE_HEADING(
                    f"\nSeeding marketplace: {tenant.name} ({vertical})"
                )
            )

            try:
                module_path = f"verticals.{vertical}.seeds.partners"
                module = importlib.import_module(module_path)
                partners_config = getattr(module, "PARTNERS", [])
            except ModuleNotFoundError:
                continue

            for pdata in partners_config:

                partner = Partner.objects.filter(
                    tenant=tenant,
                    code=pdata.get("code")
                ).first()

                if not partner:
                    continue

                products = pdata.get("products", [])

                for prod in products:

                    category = None

                    category_code = prod.get("category_code")
                    if category_code:
                        category = Category.objects.filter(
                            tenant=tenant,
                            code=category_code,
                            scope="partners.service_category"
                        ).first()

                    # ✅ CREATE PRODUCT (CATALOG)
                    mp, created = MarketplaceProduct.objects.update_or_create(
                        tenant=tenant,
                        partner=partner,
                        code=prod.get("code"),
                        defaults={
                            "name": prod.get("name"),
                            "type": MarketplaceProduct.TYPE_SERVICE,
                            "category": category,
                            "is_active": True,
                        }
                    )

                    if created:
                        total_product_created += 1

                    # ✅ CREATE LISTING (OFFER)
                    listing, l_created = PartnerListing.objects.update_or_create(
                        tenant=tenant,
                        partner=partner,
                        product=mp,
                        defaults={
                            "price": prod.get("price"),
                            "duration_minutes": prod.get("duration_minutes", 60),
                            "stock": None,
                            "is_active": True,
                        }
                    )

                    if l_created:
                        total_listing_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\nMarketplace seeded:\n"
                f"Products Created: {total_product_created}\n"
                f"Listings Created: {total_listing_created}"
            )
        )