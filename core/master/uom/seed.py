# core/master/uom/seed.py

DEFAULT_UOM_CATEGORIES = [
    {"code": "UNIT", "name": "Unit"},
    {"code": "WEIGHT", "name": "Weight"},
    {"code": "VOLUME", "name": "Volume"},
]

def seed_uom_categories(tenant):
    from .models import UOMCategory

    for cat in DEFAULT_UOM_CATEGORIES:
        UOMCategory.objects.get_or_create(
            tenant=tenant,
            code=cat["code"],
            defaults={"name": cat["name"]},
        )
