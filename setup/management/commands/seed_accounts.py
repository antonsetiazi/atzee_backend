# setup/management/commands/seed_accounts.py

import importlib
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant
from accounting.models import Account


class Command(BaseCommand):
    help = "Seed chart of accounts per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise Exception("seed_accounts cannot run in production.")

        tenants = Tenant.objects.all()

        total_created = 0
        total_updated = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.accounts"
                module = importlib.import_module(module_path)
                accounts_config = getattr(module, "ACCOUNTS", None)

                if accounts_config is None:
                    raise AttributeError("ACCOUNTS not found")

            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(f"No account seed for '{vertical}'")
                )
                continue

            except AttributeError:
                self.stdout.write(
                    self.style.WARNING(f"ACCOUNTS config missing in '{module_path}'")
                )
                continue

            self.stdout.write(f"Seeding accounts for {tenant.name} ({vertical})")

            for item in accounts_config:
                c, u = self._process_recursive(
                    tenant=tenant,
                    item=item,
                    parent=None,
                )
                total_created += c
                total_updated += u

        self.stdout.write(
            self.style.SUCCESS(
                f"Accounts seeded. Created: {total_created}, Updated: {total_updated}"
            )
        )

    def _process_recursive(self, *, tenant, item, parent):
        code = item["code"]
        name = item["name"]
        account_type = item["account_type"]
        normal_balance = item["normal_balance"]
        is_group = item.get("is_group", False)
        children = item.get("children", [])

        obj = Account.objects.filter(
            tenant=tenant,
            code=code,
            is_deleted=False
        ).first()

        created = 0
        updated = 0

        if obj:
            is_changed = False

            if obj.name != name:
                obj.name = name
                is_changed = True

            if obj.account_type != account_type:
                obj.account_type = account_type
                is_changed = True

            if obj.normal_balance != normal_balance:
                obj.normal_balance = normal_balance
                is_changed = True

            if obj.parent_id != (parent.id if parent else None):
                obj.parent = parent
                is_changed = True

            if obj.is_group != is_group:
                obj.is_group = is_group
                is_changed = True

            if is_changed:
                obj.save()
                updated = 1
                self.stdout.write(f"Updated account: {code}")

        else:
            obj = Account.objects.create(
                tenant=tenant,
                code=code,
                name=name,
                account_type=account_type,
                normal_balance=normal_balance,
                parent=parent,
                is_group=is_group,
            )
            created = 1
            self.stdout.write(f"Created account: {code}")

        for child in children:
            c, u = self._process_recursive(
                tenant=tenant,
                item=child,
                parent=obj,
            )
            created += c
            updated += u

        return created, updated