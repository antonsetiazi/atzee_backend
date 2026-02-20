# setup/management/commands/reset_ui_permissions.py


from django.core.management.base import BaseCommand
from django.db import transaction

from core.permissions.models import Permission, RolePermission
from core.ui.models import UIPage, UIMenu


class Command(BaseCommand):
    help = "Reset all UI pages, menus, and permissions, then re-seed."

    def add_arguments(self, parser):
        parser.add_argument(
            "--yes",
            action="store_true",
            help="Skip confirmation prompt"
        )

    @transaction.atomic
    def handle(self, *args, **options):

        if not options["yes"]:
            confirm = input(
                "⚠ This will DELETE all UI pages, menus, permissions. Continue? (yes/no): "
            )
            if confirm.lower() != "yes":
                self.stdout.write(self.style.WARNING("Aborted."))
                return

        self.stdout.write("🧹 Deleting RolePermissions...")
        RolePermission.objects.all().delete()

        self.stdout.write("🧹 Deleting Permissions...")
        Permission.objects.all().delete()

        self.stdout.write("🧹 Deleting UI Pages...")
        UIPage.objects.all().delete()

        self.stdout.write("🧹 Deleting UI Menus...")
        UIMenu.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS("✅ UI & Permission data successfully cleared.")
        )