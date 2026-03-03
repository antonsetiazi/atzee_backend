# verticals/pesantren/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "Pesantren",
    "code": "pesantren",
    "vertical": "pesantren",
    "is_active": True,
})
