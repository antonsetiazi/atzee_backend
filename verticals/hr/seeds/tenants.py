# verticals/hr/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed(
    {
        "name": "HR",
        "code": "hr",
        "vertical": "hr",
        "is_active": True,
    }
)
