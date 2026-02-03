# core/dashboard/cache.py

def dashboard_cache_key(*, tenant_id, context: str) -> str:
    return f"dashboard:{tenant_id}:{context}"
