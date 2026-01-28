# core/roles/management/commands/sync_roles.py
from django.core.management.base import BaseCommand
from core.roles.models import Role
from core.tenants.models import Tenant

class Command(BaseCommand):
    def handle(self, *args, **options):
        for tenant in Tenant.objects.all():
            Role.objects.get_or_create(
                tenant=tenant,
                name="Admin",
                defaults={"access_level": 100}
            )
            Role.objects.get_or_create(
                tenant=tenant,
                name="User",
                defaults={"access_level": 10}
            )
