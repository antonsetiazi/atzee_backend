# setup/management/commands/seed_notifications.py

import importlib

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction
from django.contrib.auth import get_user_model

from core.tenants.models import Tenant
from core.notifications.models import Notification
from core.notifications.events import EVENT_META

User = get_user_model()


class Command(BaseCommand):
    help = "Seed notifications per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("seed_notifications cannot run in production.")

        tenants = Tenant.objects.filter(is_active=True)

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_created = 0
        total_updated = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.notifications"
                notifications_module = importlib.import_module(module_path)
                notifications_config = getattr(
                    notifications_module,
                    "NOTIFICATIONS",
                    []
                )
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(
                        f"No notifications module found for vertical '{vertical}'"
                    )
                )
                continue

            self.stdout.write(
                f"Seeding notifications for tenant: {tenant.name} ({vertical})"
            )

            # 🔥 Ambil user dalam tenant tersebut saja (lebih proper)
            users = User.objects.filter(
                tenant_memberships__tenant=tenant,
                tenant_memberships__is_active=True,
                is_active=True,
            ).distinct()

            for user in users:
                for item in notifications_config:

                    event = item["event"]
                    meta = EVENT_META.get(event, {})
                    level = meta.get("level", "info")

                    notification, created = Notification.objects.update_or_create(
                        tenant=tenant,
                        user=user,
                        event=event,
                        title=item["title"],
                        defaults={
                            "message": item["message"],
                            "level": level,
                            "entity_type": item.get("entity_type"),
                            "entity_id": item.get("entity_id"),
                            "payload": item.get("payload"),
                            "is_read": False,
                        },
                    )

                    if created:
                        total_created += 1
                    else:
                        total_updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Notifications seeded. Created: {total_created}, Updated: {total_updated}"
        ))