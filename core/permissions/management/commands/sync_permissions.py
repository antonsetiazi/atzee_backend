# core/permissions/management/commands/sync_permissions.py

from django.core.management.base import BaseCommand
from core.permissions.registry import PermissionRegistry
from core.permissions.models import Permission
from core.tenants.models import Tenant

class Command(BaseCommand):
    help = "Sync registered permissions to database"

    def handle(self, *args, **options):
        for tenant in Tenant.objects.all():
            for perm in PermissionRegistry.all():
                print(perm)
                Permission.objects.get_or_create(
                    tenant=tenant,
                    code=perm["code"],
                    defaults={
                        "description": perm.get("description", "")
                    }
                )
