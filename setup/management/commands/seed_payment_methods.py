# setup/management/commands/seed_payment_methods.py

from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from business.payment_gateway.models import PaymentMethod


class Command(BaseCommand):
    help = "Seed payment methods (real channels) for all tenants"

    def handle(self, *args, **options):
        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        # 🔥 REALISTIC PAYMENT CHANNELS (INDONESIA)
        default_methods = [
            # =========================
            # MIDTRANS (E-WALLET)
            # =========================
            {
                "code": "gopay",
                "name": "GoPay",
                "provider": PaymentMethod.PROVIDER_MIDTRANS,
                "order": 1,
            },
            {
                "code": "shopeepay",
                "name": "ShopeePay",
                "provider": PaymentMethod.PROVIDER_MIDTRANS,
                "order": 2,
            },

            # =========================
            # MIDTRANS (BANK VA)
            # =========================
            {
                "code": "bca_va",
                "name": "BCA Virtual Account",
                "provider": PaymentMethod.PROVIDER_MIDTRANS,
                "order": 3,
            },
            {
                "code": "bni_va",
                "name": "BNI Virtual Account",
                "provider": PaymentMethod.PROVIDER_MIDTRANS,
                "order": 4,
            },
            {
                "code": "bri_va",
                "name": "BRI Virtual Account",
                "provider": PaymentMethod.PROVIDER_MIDTRANS,
                "order": 5,
            },

            # =========================
            # MIDTRANS (QRIS)
            # =========================
            {
                "code": "qris",
                "name": "QRIS",
                "provider": PaymentMethod.PROVIDER_MIDTRANS,
                "order": 6,
            },

            # =========================
            # XENDIT (OPTIONAL)
            # =========================
            {
                "code": "xendit_va",
                "name": "Virtual Account (Xendit)",
                "provider": PaymentMethod.PROVIDER_XENDIT,
                "order": 10,
            },
        ]

        for tenant in tenants:
            with transaction.atomic():
                for method in default_methods:
                    PaymentMethod.objects.update_or_create(
                        tenant=tenant,
                        code=method["code"],
                        defaults={
                            "name": method["name"],
                            "provider": method["provider"],
                            "order": method["order"],
                            "is_active": True,  # 🔥 aktif semua by default
                        },
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"✔ Payment methods seeded for tenant: {tenant.code or tenant.name}"
                )
            )