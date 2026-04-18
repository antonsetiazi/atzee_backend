# setup/management/commands/seed_banks.py

import importlib

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from core.master.banks import selectors, services


class Command(BaseCommand):
    help = "Seed banks per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise Exception("seed_banks cannot run in production.")

        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(
                self.style.WARNING("No tenants found.")
            )
            return

        total_created = 0
        total_updated = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.banks"

                bank_module = importlib.import_module(
                    module_path
                )

                banks_config = getattr(
                    bank_module,
                    "BANKS",
                    None,
                )

                if banks_config is None:
                    raise AttributeError("BANKS not found")

            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(
                        f"No bank seed found for vertical '{vertical}'"
                    )
                )
                continue

            except AttributeError:
                self.stdout.write(
                    self.style.WARNING(
                        f"BANKS config not found in '{module_path}'"
                    )
                )
                continue

            self.stdout.write(
                f"Seeding banks for {tenant.name} ({vertical})"
            )

            for item in banks_config:
                created, updated = self._process_item(
                    tenant=tenant,
                    item=item,
                )

                total_created += created
                total_updated += updated

        self.stdout.write(
            self.style.SUCCESS(
                f"Banks seeded. Created: {total_created}, Updated: {total_updated}"
            )
        )

    def _process_item(self, *, tenant, item):
        code = item["code"]
        name = item["name"]
        short_name = item.get("short_name", "")
        sort_order = item.get("sort_order", 0)

        obj = selectors.get_bank_queryset(
            tenant=tenant
        ).filter(
            code=code
        ).first()

        created = 0
        updated = 0

        if obj:
            is_changed = False

            if obj.name != name:
                obj.name = name
                is_changed = True

            if obj.short_name != short_name:
                obj.short_name = short_name
                is_changed = True

            if obj.sort_order != sort_order:
                obj.sort_order = sort_order
                is_changed = True

            if not obj.is_active:
                obj.is_active = True
                is_changed = True

            if is_changed:
                obj.save()
                updated = 1
                self.stdout.write(
                    f"Updated bank: {code}"
                )

        else:
            services.create_bank(
                tenant=tenant,
                created_by=None,
                code=code,
                name=name,
                short_name=short_name,
            )

            obj = selectors.get_bank_queryset(
                tenant=tenant
            ).get(code=code)

            obj.sort_order = sort_order
            obj.save()

            created = 1

            self.stdout.write(
                f"Created bank: {code}"
            )

        return created, updated