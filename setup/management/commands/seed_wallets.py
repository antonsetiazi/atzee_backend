# setup/management/commands/seed_wallets.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from core.tenants.models import Tenant, UserTenant
from core.wallet.models import Wallet

User = get_user_model()

class Command(BaseCommand):
    help = "Seed default wallets for all active users (for testing/dev only)"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding wallets for all active users...")

        tenants = Tenant.objects.filter(is_active=True)
        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No active tenants found."))
            return

        total_created = 0
        total_updated = 0

        for tenant in tenants:
            # Ambil semua user aktif di tenant ini
            user_tenants = UserTenant.objects.filter(tenant=tenant, is_active=True)
            for ut in user_tenants:
                user = ut.user

                wallet, created = Wallet.objects.update_or_create(
                    tenant=tenant,
                    user=user,
                    defaults={
                        "balance": 10000000  # default balance untuk testing
                    }
                )

                if created:
                    total_created += 1
                    self.stdout.write(self.style.SUCCESS(
                        f"Created wallet for {user.email} with 10,000,000 IDR"
                    ))
                else:
                    total_updated += 1
                    self.stdout.write(
                        f"Updated wallet for {user.email} to 10,000,000 IDR"
                    )

        self.stdout.write(self.style.SUCCESS(
            f"Seeding completed. {total_created} wallets created, {total_updated} wallets updated."
        ))