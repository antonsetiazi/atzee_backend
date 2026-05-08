# setup/management/commands/seed_journal_mappings.py

import importlib

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from accounting.models import (
    Account,
    JournalMapping,
)
from core.tenants.models import Tenant


class Command(BaseCommand):

    help = "Seed journal mappings"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        if not settings.DEBUG:
            raise Exception("Cannot run in production")

        tenants = Tenant.objects.all()

        for tenant in tenants:

            vertical = tenant.vertical

            try:

                module_path = (
                    f"verticals." f"{vertical}." f"seeds.journal_mappings"
                )

                module = importlib.import_module(module_path)

                configs = getattr(
                    module,
                    "JOURNAL_MAPPINGS",
                )

            except Exception:
                continue

            self.stdout.write(f"Tenant: {tenant.name}")

            for item in configs:

                account = Account.objects.get(
                    tenant=tenant,
                    code=item["account_code"],
                )

                obj, created = JournalMapping.objects.update_or_create(
                    tenant=tenant,
                    transaction_type=item["transaction_type"],
                    order=item["order"],
                    defaults={
                        "entry_type": item["entry_type"],
                        "account": account,
                        "amount_source": item["amount_source"],
                    },
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Created " f"{item['transaction_type']}"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Updated " f"{item['transaction_type']}"
                        )
                    )
