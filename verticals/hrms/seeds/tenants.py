# verticals/hrms/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "HRMS",
    "code": "hrms",
    "vertical": "hrms",
    "is_active": True,
})
