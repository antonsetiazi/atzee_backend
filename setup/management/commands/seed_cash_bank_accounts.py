# setup/management/commands/seed_cash_bank_accounts.py

import importlib

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from accounting.models import (
    Account,
    CashBankAccount,
)
from core.tenants.models import Tenant


class Command(BaseCommand):

    help = "Seed cash bank accounts " "per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("Cannot run in production")

        tenants = Tenant.objects.all()

        for tenant in tenants:

            vertical = tenant.vertical

            try:

                module_path = (
                    f"verticals." f"{vertical}." f"seeds.cash_bank_accounts"
                )

                module = importlib.import_module(module_path)

                configs = getattr(module, "CASH_BANK_ACCOUNTS")

            except Exception:

                self.stdout.write(
                    self.style.WARNING(f"No cash bank seed " f"for {vertical}")
                )

                continue

            self.stdout.write(f"Tenant: {tenant.name}")

            for item in configs:

                account = Account.objects.get(
                    tenant=tenant, code=item["account_code"]
                )

                obj, created = CashBankAccount.objects.update_or_create(
                    tenant=tenant,
                    code=item["code"],
                    defaults={
                        "name": item["name"],
                        "accounting_account": account,
                        "bank_account_number": item["account_number"],
                        "bank_name": item.get("bank_name", ""),
                        "account_holder_name": "PT Atzee Indonesia",
                        "account_type": item.get("account_type", "bank"),
                        "is_active": True,
                    },
                )

                if created:

                    self.stdout.write(
                        self.style.SUCCESS(f"Created {obj.name}")
                    )

                else:

                    self.stdout.write(
                        self.style.WARNING(f"Updated {obj.name}")
                    )
