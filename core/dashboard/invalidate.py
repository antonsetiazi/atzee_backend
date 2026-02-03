# core/dashboard/invalidate.py

from django.core.cache import cache
from core.dashboard.cache import dashboard_cache_key
from core.dashboard.registry import DASHBOARD_REGISTRY


def invalidate_dashboard_for_tenant(tenant_id):
    for context in DASHBOARD_REGISTRY.keys():
        key = dashboard_cache_key(
            tenant_id=tenant_id,
            context=context,
        )
        cache.delete(key)
