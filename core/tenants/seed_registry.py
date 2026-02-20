# core/tenants/seed_registry.py

TENANT_SEED_REGISTRY = []


def register_tenant_seed(data: dict):
    TENANT_SEED_REGISTRY.append(data)


def all_tenant_seeds():
    return TENANT_SEED_REGISTRY
