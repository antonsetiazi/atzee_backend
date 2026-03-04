# verticals/agri/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "Agri",
    "code": "agri",
    "vertical": "agri",
    "is_active": True,
})
