# setup/management/commands/seed_depreciation_entries.py

from datetime import date

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from accounting.models import DepreciationEntry, FixedAsset
from core.tenants.models import Tenant


class Command(BaseCommand):

    help = "Seed depreciation entries"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        if not settings.DEBUG:
            raise Exception("Cannot run in production")

        tenants = Tenant.objects.all()

        for tenant in tenants:

            assets = FixedAsset.objects.filter(tenant=tenant)

            if not assets.exists():
                continue

            self.stdout.write(f"Tenant: {tenant.name}")

            created_count = 0

            for asset in assets[:5]:  # ambil 5 asset pertama

                # simulate 3 bulan depreciation history
                for i in range(1, 4):

                    period = date(2025, i, 28)

                    depreciation_amount = (
                        asset.purchase_cost / asset.useful_life_months
                    )

                    accumulated = depreciation_amount * i
                    book_value = asset.purchase_cost - accumulated

                    DepreciationEntry.objects.get_or_create(
                        tenant=tenant,
                        asset=asset,
                        period_date=period,
                        defaults={
                            "depreciation_amount": depreciation_amount,
                            "accumulated_depreciation": accumulated,
                            "book_value_after": book_value,
                            "notes": f"Auto seed depreciation month {i}",
                            "status": "posted",
                        },
                    )

                    created_count += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f"Created depreciation entries: {created_count}"
                )
            )
