# verticals/research/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "Research",
    "code": "research",
    "vertical": "research",
    "is_active": True,
})
