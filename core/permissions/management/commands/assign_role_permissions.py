# core/permissions/management/commands/assign_role_permissions.py
from django.core.management.base import BaseCommand
from core.permissions.models import Permission, RolePermission
from core.roles.models import Role

class Command(BaseCommand):
    def handle(self, *args, **options):
        for role in Role.objects.all():
            perms = Permission.objects.filter(tenant=role.tenant)

            for perm in perms:
                RolePermission.objects.get_or_create(
                    role=role,
                    permission=perm
                )
