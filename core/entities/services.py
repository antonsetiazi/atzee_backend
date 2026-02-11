# core/entities/services.py

from core.permissions.services import PermissionService
from .registry import get_entity


class EntityQueryService:

    @staticmethod
    def execute(*, user, tenant, domain: str, entity_key: str, query: dict):
        # print("EntityQueryService | execute")
        # print("domain: ", domain)
        # print("entity_key: ", entity_key)
        entity = get_entity(domain, entity_key)
        # print("EntityQueryService | entity: ", entity)

        if not entity:
            raise ValueError("Entity not registered")

        if not PermissionService.can_access(
            user=user,
            tenant=tenant,
            permission_code=entity.permission,
        ):
            raise PermissionError()

        return entity.query(
            user=user,
            tenant=tenant,
            query=query,
        )


class EntityExecuteService:

    @staticmethod
    def execute(*, user, tenant, domain: str, entity_key: str, data: dict):
        entity = get_entity(domain, entity_key)

        if not entity:
            raise ValueError("Entity not registered")

        if not PermissionService.can_access(
            user=user,
            tenant=tenant,
            permission_code=entity.permission,
        ):
            raise PermissionError()

        # panggil execute() entity
        return entity.execute(
            user=user,
            tenant=tenant,
            data=data,
        )