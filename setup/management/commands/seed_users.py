# setup/management/commands/seed_users.py

from importlib import import_module
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.roles.models import Role, UserRole
from core.tenants.models import Tenant, UserTenant
from core.users.seed_registry import all_user_seeds, reset_registry


User = get_user_model()


class Command(BaseCommand):
    help = "Seed default users from verticals dynamically"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding default users...")

        tenants = Tenant.objects.filter(is_active=True)

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No active tenants found."))
            return

        # Reset the seed registry
        reset_registry()

        for tenant in tenants:
            vertical = tenant.vertical

            # Dynamic import vertical user seeds
            try:
                import_module(f"verticals.{vertical}.seeds.users")
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(f"No user seeds found for vertical '{vertical}'")
                )
                continue

        for data in all_user_seeds():
            try:
                tenant_obj = Tenant.objects.get(code=data["tenant_code"])
            except Tenant.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Tenant not found for user {data['email']}")
                )
                continue

            user, created = User.objects.update_or_create(
                email=data["email"],
                defaults={
                    "username": data["email"],
                    "full_name": data["full_name"],
                    "is_staff": data.get("is_staff", False),
                    "is_superuser": data.get("is_superuser", False),
                    "is_active": True,
                }
            )

            if created:
                user.set_password(data["password"])
                user.save()

            # ensure membership
            UserTenant.objects.update_or_create(
                user=user,
                tenant=tenant_obj,
                defaults={"is_active": True}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Created user: {user.email}"
                ))
            else:
                self.stdout.write(
                    f"Updated user: {user.email}"
                )

            role_name = data.get("role")

            if role_name:
                role = Role.objects.get(
                    tenant=tenant_obj,
                    name=role_name
                )

                UserRole.objects.update_or_create(
                    user=user,
                    role=role
                )

        self.stdout.write(self.style.SUCCESS("All default users seeded successfully."))
    