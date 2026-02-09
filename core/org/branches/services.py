# core/org/branches/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.org.branches.models import Branch
from core.org.branches import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


@transaction.atomic
def create_branch(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    description: Optional[str] = None,
) -> Branch:

    code = _normalize_str(code)
    name = name.strip()

    if description is None:
        description = ""
    else:
        description = description.strip()

    if Branch.objects.filter(
        tenant=tenant,
        code=code,
        is_deleted=False
    ).exists():
        raise ValidationError("Branch with this code already exists.")

    return Branch.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        description=description,
        created_by=created_by,
    )


@transaction.atomic
def update_branch(
    *,
    tenant: Tenant,
    branch_id: int,
    updated_by: User,
    name: Optional[str] = None,
    description: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Branch:

    branch = selectors.get_branch_by_id(
        tenant=tenant,
        branch_id=branch_id
    )

    if not branch:
        raise ValidationError("Branch not found.")

    if name is not None:
        branch.name = name
    if description is not None:
        branch.description = description
    if is_active is not None:
        branch.is_active = is_active

    branch.updated_by = updated_by
    branch.save()

    return branch


@transaction.atomic
def delete_branch(
    *,
    tenant: Tenant,
    branch_id: int,
    deleted_by: User
) -> None:

    branch = selectors.get_branch_by_id(
        tenant=tenant,
        branch_id=branch_id
    )

    if not branch:
        raise ValidationError("Branch not found.")

    branch.is_deleted = True
    branch.updated_by = deleted_by
    branch.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
