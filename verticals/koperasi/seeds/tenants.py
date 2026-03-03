# verticals/koperasi/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "Koperasi",
    "code": "koperasi",
    "vertical": "koperasi",
    "is_active": True,
})
