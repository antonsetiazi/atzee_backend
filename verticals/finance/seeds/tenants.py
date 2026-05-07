# verticals/finance/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "FINANCE",
    "code": "finance",
    "vertical": "finance",
    "is_active": True,
})
