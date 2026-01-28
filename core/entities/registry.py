# core/entities/registry.py

from typing import Dict
from .contracts import BaseEntity

from core.permissions.registry import PermissionRegistry

ENTITY_REGISTRY: Dict[str, BaseEntity] = {}


def register_entity(entity: BaseEntity):
    # print("register_entity | entity.key:", entity.key)
    if entity.key in ENTITY_REGISTRY:
        raise ValueError(f"Entity '{entity.key}' already registered")

    ENTITY_REGISTRY[entity.key] = entity

    # 🔐 REGISTER PERMISSION (jika ada)
    permission = getattr(entity, "permission", None)
    if permission:
        PermissionRegistry.register([
        {"code": permission, "description": f"Permission for entity '{entity.key}'"}
    ])


def get_entity(entity_key: str) -> BaseEntity | None:
    # print("get_entity | ENTITY_REGISTRY :", ENTITY_REGISTRY)
    return ENTITY_REGISTRY.get(entity_key)
