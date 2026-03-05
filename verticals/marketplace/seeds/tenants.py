# verticals/marketplace/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "Marketplace",
    "code": "marketplace",
    "vertical": "marketplace",
    "is_active": True,
})
