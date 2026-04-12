# setup/management/commands/import_indonesia_geo.py

from django.core.management.base import BaseCommand
from setup.management.commands.seed_geo import import_indonesia_geo


class Command(BaseCommand):
    help = "Import complete Indonesia geo master"

    def handle(self, *args, **kwargs):
        import_indonesia_geo()
        self.stdout.write(
            self.style.SUCCESS(
                "Indonesia geo import completed successfully."
            )
        )