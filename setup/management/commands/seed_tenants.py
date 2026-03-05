# setup/management/commands/seed_tenants.py

from django.core.management.base import BaseCommand
from core.tenants.models import Tenant
from core.tenants.seed_registry import all_tenant_seeds


class Command(BaseCommand):
    help = "Seed default tenants"

    def handle(self, *args, **kwargs):
        # Import semua vertical seed
        import verticals.agri.seeds.tenants
        import verticals.bengkel.seeds.tenants
        import verticals.cbs.seeds.tenants
        import verticals.distributor.seeds.tenants
        import verticals.hrms.seeds.tenants
        import verticals.isp.seeds.tenants
        import verticals.koperasi.seeds.tenants
        import verticals.pesantren.seeds.tenants
        import verticals.pos.seeds.tenants
        import verticals.research.seeds.tenants
        import verticals.ustadzku.seeds.tenants

        for data in all_tenant_seeds():
            obj, created = Tenant.objects.update_or_create(
                code=data["code"],
                defaults={
                    "name": data["name"],
                    "vertical": data["vertical"],
                    "is_active": data.get("is_active", True),
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Created tenant: {obj.code}"
                ))
            else:
                self.stdout.write(
                    f"Updated tenant: {obj.code}"
                )
