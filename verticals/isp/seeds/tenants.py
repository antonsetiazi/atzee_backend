# verticals/isp/seeds/tenants.py

from core.tenants.seed_registry import register_tenant_seed

register_tenant_seed({
    "name": "ISP",
    "code": "isp",
    "vertical": "isp",
    "is_active": True,
})
