# setup/management/commands/seed_partners.py

import importlib

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction
from django.contrib.auth import get_user_model

from core.tenants.models import Tenant
from business.partners.models import Partner
from business.partners.models import PartnerServiceProfile

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

                service_profile_data = data.get("service_profile")
                if service_profile_data:
                    PartnerServiceProfile.objects.update_or_create(
                        partner=partner,
                        defaults={
                            "specialization": service_profile_data.get("specialization"),
                            "experience_years": service_profile_data.get("experience_years", 0),
                            "bio": service_profile_data.get("bio"),
                        }
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


        # ─────────────────────────────────────────────
        # SUMMARY
        # ─────────────────────────────────────────────
        self.stdout.write(
            self.style.SUCCESS(
                "\nSeeding completed:\n"
                f"Partners Created: {total_partner_created}\n"
                f"Partners Updated: {total_partner_updated}"
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

        # Gunakan partner.core_user sebagai owner
        partner_user = partner.core_user
        if not partner_user:
            return  # skip kalau partner tidak punya core_user

        File.objects.update_or_create(
            tenant=tenant,
            related_entity="partner_image",
            related_id=str(partner.id),
            defaults={
                "file": final_path,
                "original_name": image_filename,
                "mime_type": "image/jpeg",
                "size": len(content),
                "owner": partner_user,
                "created_by": partner_user,
                "updated_by": partner_user,
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