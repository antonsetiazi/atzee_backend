# setup/management/commands/seed_fixed_assets.py

import importlib

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from accounting.models import AssetCategory, FixedAsset
from core.tenants.models import Tenant


class Command(BaseCommand):

    help = "Seed fixed assets"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        if not settings.DEBUG:
            raise Exception("Cannot run in production")

        tenants = Tenant.objects.all()

        for tenant in tenants:

            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.fixed_assets"

                module = importlib.import_module(module_path)
                configs = getattr(module, "FIXED_ASSETS")

            except Exception:
                continue

            self.stdout.write(f"Tenant: {tenant.name}")

            for item in configs:

                category = AssetCategory.objects.get(
                    tenant=tenant,
                    code=item["category_code"],
                )

                obj, created = FixedAsset.objects.update_or_create(
                    tenant=tenant,
                    asset_number=item["asset_number"],
                    defaults={
                        "name": item["name"],
                        "description": item.get("description", ""),
                        "category": category,
                        "purchase_date": item["purchase_date"],
                        "capitalization_date": item["capitalization_date"],
                        "purchase_cost": item["purchase_cost"],
                        "salvage_value": item.get("salvage_value", 0),
                        "depreciation_method": item["depreciation_method"],
                        "useful_life_months": item["useful_life_months"],
                        "depreciation_start_date": item[
                            "depreciation_start_date"
                        ],
                        "accumulated_depreciation": item.get(
                            "accumulated_depreciation", 0
                        ),
                        "book_value": item.get("book_value", 0),
                        "status": item.get("status", "active"),
                    },
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Created {item['asset_number']}")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Updated {item['asset_number']}")
                    )
