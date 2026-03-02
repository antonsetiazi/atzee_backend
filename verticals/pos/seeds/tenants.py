# verticals/pos/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "P.O.S",
    "code": "pos",
    "vertical": "pos",
    "is_active": True,
})
