# setup/management/commands/seed_asset_categories.py

import importlib

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from accounting.models import Account, AssetCategory
from core.tenants.models import Tenant


class Command(BaseCommand):

    help = "Seed asset categories"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        if not settings.DEBUG:
            raise Exception("Cannot run in production")

        tenants = Tenant.objects.all()

        for tenant in tenants:

            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.asset_categories"

                module = importlib.import_module(module_path)
                configs = getattr(module, "ASSET_CATEGORIES")

            except Exception:
                continue

            self.stdout.write(f"Tenant: {tenant.name}")

            for item in configs:

                asset_acc = Account.objects.get(
                    tenant=tenant,
                    code=item["asset_account_code"],
                )

                acc_dep = Account.objects.get(
                    tenant=tenant,
                    code=item["accumulated_account_code"],
                )

                exp_acc = Account.objects.get(
                    tenant=tenant,
                    code=item["expense_account_code"],
                )

                obj, created = AssetCategory.objects.update_or_create(
                    tenant=tenant,
                    code=item["code"],
                    defaults={
                        "name": item["name"],
                        "description": item.get("description", ""),
                        "depreciation_method": item["depreciation_method"],
                        "useful_life_months": item["useful_life_months"],
                        "salvage_value_percent": item["salvage_value_percent"],
                        "asset_account": asset_acc,
                        "accumulated_depreciation_account": acc_dep,
                        "depreciation_expense_account": exp_acc,
                    },
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Created {item['code']}")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Updated {item['code']}")
                    )
