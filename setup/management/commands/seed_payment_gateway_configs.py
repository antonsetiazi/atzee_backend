# setup/management/commands/seed_payment_gateway_configs.py

# setup/management/commands/seed_payment_gateway_configs.py

from django.core.management.base import BaseCommand
from django.db import transaction

from core.tenants.models import Tenant
from business.payment_gateway.models import PaymentGatewayConfig


class Command(BaseCommand):
    help = "Seed payment gateway configs (Midtrans, Xendit) for all tenants"

    def handle(self, *args, **options):
        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        # 🔥 DEFAULT CONFIG TEMPLATE
        default_configs = [
            {
                "provider": PaymentGatewayConfig.PROVIDER_MIDTRANS,
                "environment": PaymentGatewayConfig.ENV_SANDBOX,
                "api_key": "SB-Mid-server-wOhux155wpT66W9A38KtCZoZ",   # 🔥 GANTI NANTI
                "secret_key": "",                        # optional
                "merchant_id": "G879347415",
                "is_active": True,
                "extra_config": {},
            },
            {
                "provider": PaymentGatewayConfig.PROVIDER_XENDIT,
                "environment": PaymentGatewayConfig.ENV_SANDBOX,
                "api_key": "YOUR_XENDIT_API_KEY",
                "secret_key": "",
                "merchant_id": "",
                "is_active": False,  # default non aktif
                "extra_config": {},
            },
        ]

        for tenant in tenants:
            with transaction.atomic():
                for cfg in default_configs:
                    PaymentGatewayConfig.objects.update_or_create(
                        tenant=tenant,
                        provider=cfg["provider"],
                        defaults={
                            "environment": cfg["environment"],
                            "api_key": cfg["api_key"],
                            "secret_key": cfg["secret_key"],
                            "merchant_id": cfg["merchant_id"],
                            "is_active": cfg["is_active"],
                            "extra_config": cfg["extra_config"],
                        },
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"✔ Payment gateway configs seeded for tenant: {tenant.code or tenant.name}"
                )
            )