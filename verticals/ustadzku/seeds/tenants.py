# verticals/ustadzku/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "Ustadzku Main",
    "code": "ustadzku",
    "vertical": "ustadzku",
    "is_active": True,
})
