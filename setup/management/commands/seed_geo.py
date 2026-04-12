# setup/management/commands/seed_geo.py

import requests
from django.db import transaction

from core.geo.countries.models import Country
from core.geo.regions.models import Region
from core.geo.cities.models import City
from core.geo.districts.models import District
from core.geo.villages.models import Village


BASE_URL = "https://wilayah.id/api"


def fetch_json(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()["data"]


@transaction.atomic
def import_indonesia_geo():
    print("Importing Indonesia country...")

    country, _ = Country.objects.get_or_create(
        code="ID",
        defaults={"name": "Indonesia"}
    )

    # =========================
    # PROVINCES → REGIONS
    # =========================
    print("Fetching provinces...")
    provinces = fetch_json(f"{BASE_URL}/provinces.json")

    for province in provinces:
        region, _ = Region.objects.get_or_create(
            country=country,
            code=province["code"],
            defaults={
                "name": province["name"]
            }
        )

        print(f"Region: {region.name}")

        # =========================
        # CITIES
        # =========================
        cities = fetch_json(
            f"{BASE_URL}/regencies/{province['code']}.json"
        )

        for city_data in cities:
            city, _ = City.objects.get_or_create(
                country=country,
                region=region,
                code=city_data["code"],
                defaults={
                    "name": city_data["name"]
                }
            )

            print(f"  City: {city.name}")

            # # =========================
            # # DISTRICTS
            # # =========================
            # districts = fetch_json(
            #     f"{BASE_URL}/districts/{city_data['code']}.json"
            # )

            # for district_data in districts:
            #     district, _ = District.objects.get_or_create(
            #         country=country,
            #         region=region,
            #         city=city,
            #         code=district_data["code"],
            #         defaults={
            #             "name": district_data["name"]
            #         }
            #     )

            #     print(f"    District: {district.name}")

            #     # =========================
            #     # VILLAGES
            #     # =========================
            #     villages = fetch_json(
            #         f"{BASE_URL}/villages/{district_data['code']}.json"
            #     )

            #     for village_data in villages:
            #         Village.objects.get_or_create(
            #             country=country,
            #             region=region,
            #             city=city,
            #             district=district,
            #             code=village_data["code"],
            #             defaults={
            #                 "name": village_data["name"]
            #             }
            #         )