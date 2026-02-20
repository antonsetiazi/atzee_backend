# core/entities/registry.py

from typing import Dict
from .contracts import BaseEntity

from core.permissions.registry import PermissionRegistry

# domain -> entity_key -> entity
ENTITY_REGISTRY: Dict[str, Dict[str, BaseEntity]] = {}


def register_entity(entity: BaseEntity):
    domain = entity.domain
    key = entity.key

    if domain not in ENTITY_REGISTRY:
        ENTITY_REGISTRY[domain] = {}

    # print("register_entity | entity.key:", entity.key)
    if key in ENTITY_REGISTRY[domain]:
        raise ValueError(f"Entity '{domain}.{key}' already registered")

    ENTITY_REGISTRY[domain][key] = entity

    # 🔐 REGISTER PERMISSION (jika ada)
    permission = getattr(entity, "permission", None)
    if permission:
        PermissionRegistry.register([
            {
                "module": domain,
                "code": permission,
                "description": f"Permission for entity '{domain}.{key}'"
            }
        ])


def get_entity(domain: str, entity_key: str) -> BaseEntity | None:
    # print("get_entity | entity_key: ", entity_key)
    return ENTITY_REGISTRY.get(domain, {}).get(entity_key)
