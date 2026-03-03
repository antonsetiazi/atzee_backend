# verticals/bengkel/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "Bengkel",
    "code": "bengkel",
    "vertical": "bengkel",
    "is_active": True,
})
