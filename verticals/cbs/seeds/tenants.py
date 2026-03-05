# verticals/cbs/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "CBS",
    "code": "cbs",
    "vertical": "cbs",
    "is_active": True,
})
