# setup/management/commands/seed_partners.py

import importlib
import random

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction
from django.contrib.auth import get_user_model

from core.tenants.models import Tenant
from business.partners.models import Partner
from business.products.models import Product, PartnerProduct

import os
from django.core.files.base import ContentFile
from core.files.models import File
from core.files.storage import FileStorageService
from core.users.models import User
from core.roles.models import Role, UserRole
from core.tenants.models import UserTenant


User = get_user_model()

class Command(BaseCommand):
    help = "Seed partners + products per tenant based on vertical"

    @transaction.atomic
    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise Exception("seed_partners cannot run in production.")

        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.WARNING("No tenants found."))
            return

        total_partner_created = 0
        total_partner_updated = 0
        total_product_created = 0
        total_partner_product_created = 0

        for tenant in tenants:
            vertical = tenant.vertical

            self.stdout.write(
                self.style.MIGRATE_HEADING(
                    f"\nSeeding tenant: {tenant.name} ({vertical})"
                )
            )

            # ─────────────────────────────────────────────
            # LOAD PARTNER CONFIG
            # ─────────────────────────────────────────────
            try:
                partner_module_path = f"verticals.{vertical}.seeds.partners"
                partner_module = importlib.import_module(partner_module_path)
                partners_config = getattr(partner_module, "PARTNERS", [])
            except ModuleNotFoundError:
                self.stdout.write(
                    self.style.WARNING(
                        f"No partners module found for vertical '{vertical}'"
                    )
                )
                continue

            # ─────────────────────────────────────────────
            # LOAD PRODUCT CONFIG
            # ─────────────────────────────────────────────
            try:
                product_module_path = f"verticals.{vertical}.seeds.products"
                product_module = importlib.import_module(product_module_path)
                products_config = getattr(product_module, "PRODUCTS", [])
            except ModuleNotFoundError:
                products_config = []
                self.stdout.write(
                    self.style.WARNING(
                        f"No products module found for vertical '{vertical}'"
                    )
                )

            # ─────────────────────────────────────────────
            # SEED PRODUCTS
            # ─────────────────────────────────────────────
            tenant_products = []

            for pdata in products_config:
                product, created = Product.objects.update_or_create(
                    tenant=tenant,
                    code=pdata.get("code"),
                    defaults={
                        "name": pdata["name"],
                        "product_type": pdata.get("product_type", Product.TYPE_SERVICE),
                        "description": pdata.get("description"),
                    },
                )

                tenant_products.append(product)

                if created:
                    total_product_created += 1

            # ─────────────────────────────────────────────
            # SEED PARTNERS
            # ─────────────────────────────────────────────
            for data in partners_config:

                core_user = self._get_or_create_partner_user(tenant, data)

                partner, created = Partner.objects.update_or_create(
                    tenant=tenant,
                    code=data.get("code"),
                    defaults={
                        "core_user": core_user,
                        "name": data["name"],
                        "email": data.get("email"),
                        "phone": data.get("phone"),
                        "address": data.get("address"),
                        "notes": data.get("notes"),
                        "search_latitude": data.get("latitude"),
                        "search_longitude": data.get("longitude"),
                        "base_price": data.get("base_price"),
                        "rating_avg": data.get("rating_avg", 0),
                        "rating_count": data.get("rating_count", 0),
                    },
                )

                image_filename = data.get("image")

                if image_filename:
                    self._attach_partner_image(
                        tenant=tenant,
                        partner=partner,
                        image_filename=image_filename,
                    )

                if created:
                    total_partner_created += 1
                else:
                    total_partner_updated += 1

                # ─────────────────────────────────────────
                # ASSIGN 3 RANDOM PRODUCTS PER PARTNER
                # ─────────────────────────────────────────
                if tenant_products:
                    selected_products = random.sample(
                        tenant_products,
                        min(3, len(tenant_products))
                    )

                    for product in selected_products:
                        _, pp_created = PartnerProduct.objects.update_or_create(
                            tenant=tenant,
                            partner=partner,
                            product=product,
                            defaults={
                                "price": (
                                    (partner.base_price or 200000)
                                    + random.randint(-50000, 50000)
                                ),
                                "duration_minutes": random.choice([60, 90, 120]),
                                "is_active": True,
                            },
                        )

                        if pp_created:
                            total_partner_product_created += 1

        # ─────────────────────────────────────────────
        # SUMMARY
        # ─────────────────────────────────────────────
        self.stdout.write(
            self.style.SUCCESS(
                "\nSeeding completed:\n"
                f"Partners Created: {total_partner_created}\n"
                f"Partners Updated: {total_partner_updated}\n"
                f"Products Created: {total_product_created}\n"
                f"PartnerProducts Created: {total_partner_product_created}"
            )
        )


    def _get_tenant_admin(self, tenant):
        return (
            User.objects.filter(
                is_superuser=True,
                tenant_memberships__tenant=tenant
            ).first()
        )
    
    
    def _attach_partner_image(self, tenant, partner, image_filename):
        """
        Attach dummy image to partner via File model.
        """

        assets_dir = os.path.join(
            settings.BASE_DIR,
            "verticals",
            tenant.vertical,
            "seeds",
            "assets",
            "partners",
        )

        file_path = os.path.join(assets_dir, image_filename)

        if not os.path.exists(file_path):
            return

        with open(file_path, "rb") as f:
            content = f.read()

        django_file = ContentFile(content)
        django_file.name = image_filename

        storage_path = FileStorageService.build_path(
            tenant=tenant,
            filename=image_filename,
        )

        final_path = FileStorageService.save(
            path=storage_path,
            file=django_file,
        )

        admin_user = self._get_tenant_admin(tenant)

        if not admin_user:
            return  # skip kalau tidak ada user

        File.objects.update_or_create(
            tenant=tenant,
            related_entity="partner_image",
            related_id=str(partner.id),
            defaults={
                "file": final_path,
                "original_name": image_filename,
                "mime_type": "image/jpeg",
                "size": len(content),
                "owner": admin_user,
                "created_by": admin_user,
                "updated_by": admin_user,
                "is_public": True,
            },
        )

    def _get_or_create_partner_user(self, tenant, partner_data):
        """
        Ensure each partner has a core_user.
        """

        email = partner_data.get("email")
        full_name = partner_data.get("name")

        if not email:
            return None

        user, created = User.objects.update_or_create(
            email=email,
            defaults={
                "username": email,
                "full_name": full_name,
                "is_active": True,
                "is_staff": False,
                "is_superuser": False,
            }
        )

        if created:
            user.set_password("Partner123!")
            user.save()

        # Tenant membership
        UserTenant.objects.update_or_create(
            user=user,
            tenant=tenant,
            defaults={"is_active": True}
        )

        # Assign Partner role
        try:
            role = Role.objects.get(
                tenant=tenant,
                name="Partner"
            )
            UserRole.objects.update_or_create(
                user=user,
                role=role
            )
        except Role.DoesNotExist:
            pass

        return user