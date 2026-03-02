# setup/management/commands/seed_roles.py

import importlib

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction
from django.contrib.auth import get_user_model

from core.tenants.models import Tenant
from core.roles.models import Role, UserRole
from core.permissions.models import Permission, RolePermission

User = get_user_model()


class Command(BaseCommand):
    help = "Seed roles per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("seed_roles cannot run in production.")

        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_created = 0
        total_updated = 0
        total_permissions = 0

        for tenant in tenants:
            vertical = tenant.vertical

            try:
                module_path = f"verticals.{vertical}.seeds.roles"
                roles_module = importlib.import_module(module_path)
                roles_config = getattr(roles_module, "ROLES", [])
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(f"No roles module found for vertical '{vertical}'")
                )
                continue

            self.stdout.write(f"Seeding roles for tenant: {tenant.name} ({vertical})")

            for role_data in roles_config:
                role, created = Role.objects.update_or_create(
                    tenant=tenant,
                    name=role_data["name"],
                    defaults={
                        "description": role_data["description"],
                        "access_level": role_data["access_level"],
                    }
                )

                if created:
                    total_created += 1
                else:
                    total_updated += 1

                # 🔐 AUTO ASSIGN USER ROLE
                auto_assign = role_data.get("auto_assign")
                user = None
                if auto_assign == "owner":
                    users = User.objects.filter(
                        tenant_memberships__tenant=tenant,
                        is_superuser=True
                    )

                if user:
                    UserRole.objects.update_or_create(
                        user=user,
                        role=role
                    )

                # 🔑 ASSIGN DEFAULT PERMISSIONS
                for perm_code in role_data.get("default_permissions", []):
                    permission = Permission.objects.filter(
                        tenant=tenant,
                        code=perm_code
                    ).first()

                    if not permission:
                        raise Exception(
                            f"Permission '{perm_code}' not found for tenant '{tenant}'. "
                            "Make sure seed_ui runs before seed_roles."
                        )
                    
                    _, was_created = RolePermission.objects.get_or_create(
                        role=role,
                        permission=permission,
                    )
                    if was_created:
                        total_permissions += 1

        self.stdout.write(self.style.SUCCESS(
            f"Roles seeded. Created: {total_created}, Updated: {total_updated}"
        ))
