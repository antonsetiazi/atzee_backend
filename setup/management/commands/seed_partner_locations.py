# business/tracking/management/commands/seed_partner_locations.py

import random
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone

from core.tenants.models import Tenant
from business.partners.models import Partner
from business.tracking.models import PartnerLocation


# 📍 Bounding box Jabodetabek
JABODETABEK_BOUNDS = {
    "lat_min": -6.5,
    "lat_max": -6.1,
    "lng_min": 106.6,
    "lng_max": 107.1,
}


def random_location():
    return (
        round(random.uniform(JABODETABEK_BOUNDS["lat_min"], JABODETABEK_BOUNDS["lat_max"]), 6),
        round(random.uniform(JABODETABEK_BOUNDS["lng_min"], JABODETABEK_BOUNDS["lng_max"]), 6),
    )


class Command(BaseCommand):
    help = "Seed dummy partner locations (Jabodetabek)"

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true")

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise Exception("Only for development")

        tenants = Tenant.objects.all()
        total_created = 0

        for tenant in tenants:
            self.stdout.write(f"\nTenant: {tenant.name}")

            if options["reset"]:
                PartnerLocation.objects.filter(tenant=tenant).delete()
                self.stdout.write("→ Old locations cleared")

            partners = Partner.objects.filter(tenant=tenant)

            for partner in partners:
                base_lat = partner.search_latitude or -6.2
                base_lng = partner.search_longitude or 106.8

                # simulate movement (5 titik)
                for i in range(5):
                    lat_offset = random.uniform(-0.01, 0.01)
                    lng_offset = random.uniform(-0.01, 0.01)

                    PartnerLocation.objects.create(
                        tenant=tenant,
                        partner=partner,
                        latitude=round(base_lat + lat_offset, 6),
                        longitude=round(base_lng + lng_offset, 6),
                        accuracy=random.uniform(5, 20),
                    )

                    total_created += 1

        self.stdout.write(
            self.style.SUCCESS(f"\n✅ Created {total_created} location points")
        )
        