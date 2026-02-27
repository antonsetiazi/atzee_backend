# setup/management/commands/seed_payment_methods.py

from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from core.payment.models import PaymentMethod, PaymentGatewayType


class Command(BaseCommand):
    help = "Seed default Payment Methods for all tenants"

    def handle(self, *args, **options):
        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        default_methods = [
            {
                "code": "wallet",
                "name": "Internal Wallet",
                "gateway": PaymentGatewayType.WALLET,
            },
            {
                "code": "midtrans",
                "name": "Midtrans Snap",
                "gateway": PaymentGatewayType.MIDTRANS,
            },
            {
                "code": "xendit",
                "name": "Xendit Gateway",
                "gateway": PaymentGatewayType.XENDIT,
            },
        ]

        for tenant in tenants:
            with transaction.atomic():
                for method in default_methods:
                    PaymentMethod.objects.get_or_create(
                        tenant=tenant,
                        code=method["code"],
                        defaults={
                            "name": method["name"],
                            "gateway": method["gateway"],
                            "is_active": method["code"] == "wallet",
                        },
                    )

            self.stdout.write(
                self.style.SUCCESS(f"✔ Payment methods seeded for tenant: {tenant.code or tenant.name}")
            )