# setup/management/commands/seed_policies.py

import importlib
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant
from core.legal.models import PolicyDocument


class Command(BaseCommand):
    help = "Seed policies per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise Exception("seed_policies cannot run in production.")

        tenants = Tenant.objects.all()
        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_created = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.policies"
                policies_module = importlib.import_module(module_path)

                policies_config = getattr(policies_module, "POLICIES", None)
                if policies_config is None:
                    raise AttributeError("POLICIES not found")

            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(f"No policies module found for vertical '{vertical}'")
                )
                continue

            except AttributeError:
                self.stdout.write(
                    self.style.WARNING(f"POLICIES config not found in module '{module_path}'")
                )
                continue

            # =========================
            # CLEAR EXISTING (OPTIONAL)
            # =========================
            PolicyDocument.objects.filter(tenant=tenant).update(
                is_deleted=True
            )

            # =========================
            # CREATE NEW
            # =========================
            for policy_data in policies_config:
                PolicyDocument.objects.create(
                    tenant=tenant,
                    code=policy_data["code"],
                    policy_type=policy_data["policy_type"],
                    title=policy_data["title"],
                    content=policy_data["content"],
                    version=1,
                    is_active=True,
                )
                total_created += 1

            self.stdout.write(
                f"Policies seeded for tenant {tenant.name} ({vertical})"
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Policies seeded successfully. Total created: {total_created}"
            )
        )