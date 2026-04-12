# core/geo/importers/indonesia_importer.py

import json
from pathlib import Path

from core.geo.countries.models import Country
from core.geo.regions.models import Region
from core.geo.cities.models import City


BASE_DIR = Path("data/geo/indonesia")


def import_country():
    Country.objects.get_or_create(
        code="ID",
        defaults={
            "name": "Indonesia"
        }
    )


def import_regions():
    country = Country.objects.get(code="ID")

    with open(BASE_DIR / "provinces.json", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        Region.objects.get_or_create(
            country=country,
            code=item["code"],
            defaults={
                "name": item["name"]
            }
        )