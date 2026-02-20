# setup/management/commands/reset_migrations.py

import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Reset all migration files (DEV ONLY)"

    def handle(self, *args, **options):
        base_dir = Path(settings.BASE_DIR)

        self.stdout.write(self.style.WARNING(
            "⚠️  WARNING: This will delete ALL migration files except __init__.py"
        ))

        confirm = input("Type 'yes' to continue: ")
        if confirm != "yes":
            self.stdout.write("Cancelled.")
            return

        deleted = 0

        for root, dirs, files in os.walk(base_dir):
            if "migrations" in root.split(os.sep):
                for file in files:
                    if file != "__init__.py" and file.endswith(".py"):
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                        deleted += 1

        self.stdout.write(self.style.SUCCESS(
            f"Deleted {deleted} migration files."
        ))
