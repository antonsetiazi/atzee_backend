# setup/management/commands/seed_categories.py

import importlib
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction

from core.tenants.models import Tenant
from core.classifications.categories import services, selectors


class Command(BaseCommand):
    help = "Seed categories per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise Exception("seed_categories cannot run in production.")

        tenants = Tenant.objects.all()
        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_created = 0
        total_updated = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.categories"
                category_module = importlib.import_module(module_path)
                categories_config = getattr(category_module, "CATEGORIES", None)

                if categories_config is None:
                    raise AttributeError("CATEGORIES not found")

            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(f"No category seed found for vertical '{vertical}'")
                )
                continue

            except AttributeError:
                self.stdout.write(
                    self.style.WARNING(f"CATEGORIES config not found in '{module_path}'")
                )
                continue

            self.stdout.write(f"Seeding categories for {tenant.name} ({vertical})")

            for item in categories_config:
                created, updated = self._process_recursive(
                    tenant=tenant,
                    item=item,
                    parent=None,
                )
                total_created += created
                total_updated += updated

        self.stdout.write(
            self.style.SUCCESS(
                f"Categories seeded. Created: {total_created}, Updated: {total_updated}"
            )
        )

    def _process_recursive(self, *, tenant, item, parent):
        code = item["code"]
        name = item["name"]
        scope = item["scope"]
        children = item.get("children", [])

        obj = selectors.get_category_queryset(tenant=tenant).filter(
            code=code
        ).first()

        created = 0
        updated = 0

        if obj:
            is_changed = False

            if obj.name != name:
                obj.name = name
                is_changed = True

            if obj.scope != scope:
                obj.scope = scope
                is_changed = True

            if obj.parent_id != (parent.id if parent else None):
                obj.parent = parent
                is_changed = True

            if is_changed:
                obj.save()
                updated = 1
                self.stdout.write(f"Updated category: {code}")
        else:
            obj = services.create_category(
                tenant=tenant,
                created_by=None,
                code=code,
                name=name,
                scope=scope,
                parent_id=parent.id if parent else None,
            )
            created = 1
            self.stdout.write(f"Created category: {code}")

        # process children recursively
        for child in children:
            c, u = self._process_recursive(
                tenant=tenant,
                item=child,
                parent=obj,
            )
            created += c
            updated += u

        return created, updated