# verticals/distributor/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "Distributor",
    "code": "distributor",
    "vertical": "distributor",
    "is_active": True,
})
