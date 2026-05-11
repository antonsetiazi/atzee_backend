# setup/management/commands/seed_asset_disposals.py

import random
from datetime import date, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from accounting.models import AssetDisposal, FixedAsset
from core.tenants.models import Tenant


class Command(BaseCommand):

    help = "Seed asset disposals"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        if not settings.DEBUG:
            raise Exception("Cannot run in production")

        tenants = Tenant.objects.all()

        for tenant in tenants:

            assets = FixedAsset.objects.filter(
                tenant=tenant,
                status__in=["active", "fully_depreciated"],
            )

            if not assets.exists():
                continue

            self.stdout.write(f"Tenant: {tenant.name}")

            created = 0

            for asset in assets[:3]:  # hanya 3 asset saja

                disposal_value = float(asset.book_value) * random.uniform(
                    0.8, 1.2
                )

                gain_loss = disposal_value - float(asset.book_value)

                AssetDisposal.objects.get_or_create(
                    tenant=tenant,
                    asset=asset,
                    disposal_date=date.today() - timedelta(days=30),
                    defaults={
                        "disposal_value": disposal_value,
                        "gain_loss_amount": gain_loss,
                        "notes": "Auto seed disposal example",
                        "status": "posted",
                    },
                )

                created += 1

            self.stdout.write(
                self.style.SUCCESS(f"Created asset disposals: {created}")
            )
