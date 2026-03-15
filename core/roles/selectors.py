# core/roles/selectors.py

from core.roles.models import Role
from core.roles.enums import RoleCode


def get_role(*, tenant, code: RoleCode):
    return Role.objects.get(
        tenant=tenant,
        code=code,
    )