# setup/management/commands/bootstrap.py


from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Run full bootstrap (tenants, users, ui)"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("🚀 Starting full bootstrap..."))

        try:
            self.stdout.write("→ Seeding tenants...")
            call_command("seed_tenants")

            self.stdout.write("→ Seeding roles...")
            call_command("seed_roles")

            self.stdout.write("→ Seeding users...")
            call_command("seed_users")

            self.stdout.write("→ Seeding UI...")
            call_command("seed_ui")

            self.stdout.write("→ Seeding Navigation...")
            call_command("seed_navigation")

            self.stdout.write("→ Seeding Banner...")
            call_command("seed_banner")

            # 4️⃣ Ensure superadmin
            self.ensure_superadmin()
            
            self.stdout.write(
                self.style.SUCCESS("✅ Bootstrap completed successfully.")
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Bootstrap failed: {str(e)}")
            )


    def ensure_superadmin(self):
        """
        Create default platform superadmin if not exists.
        """
        email = "superadmin@platform.local"
        password = "SuperAdmin123!"

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": email,
                "full_name": "Platform Super Admin",
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            }
        )

        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"👑 Superadmin created: {email}"
                )
            )
        else:
            self.stdout.write(
                f"👑 Superadmin already exists: {email}"
            )