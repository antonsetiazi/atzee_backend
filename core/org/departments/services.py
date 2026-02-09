# core/org/departments/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.org.departments.models import Department
from core.org.departments import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


@transaction.atomic
def create_department(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    description: Optional[str] = None,
    parent_id: Optional[int] = None,
) -> Department:

    code = _normalize_str(code)
    name = name.strip()
    
    if description is None:
        description = ""
    else:
        description = description.strip()

    parent = None
    if parent_id:
        parent = selectors.get_department_by_id(
            tenant=tenant,
            department_id=int(parent_id)
        )
        if not parent:
            raise ValidationError("Parent department not found.")

    if Department.objects.filter(
        tenant=tenant,
        code=code,
        is_deleted=False
    ).exists():
        raise ValidationError("Department with this code already exists.")

    return Department.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        description=description,
        parent=parent,
        created_by=created_by,
    )


@transaction.atomic
def update_department(
    *,
    tenant: Tenant,
    department_id: int,
    updated_by: User,
    name: Optional[str] = None,
    description: Optional[str] = None,
    parent_id: Optional[int] = None,
    is_active: Optional[bool] = None,
) -> Department:

    dept = selectors.get_department_by_id(
        tenant=tenant,
        department_id=department_id
    )

    if not dept:
        raise ValidationError("Department not found.")

    if parent_id is not None:
        if parent_id == dept.id:
            raise ValidationError("Department cannot be its own parent.")

        parent = None
        if parent_id:
            parent = selectors.get_department_by_id(
                tenant=tenant,
                department_id=int(parent_id)
            )
            if not parent:
                raise ValidationError("Parent department not found.")

        dept.parent = parent

    if name is not None:
        dept.name = name
    if description is not None:
        dept.description = description
    if is_active is not None:
        dept.is_active = is_active

    dept.updated_by = updated_by
    dept.save()

    return dept


@transaction.atomic
def delete_department(
    *,
    tenant: Tenant,
    department_id: int,
    deleted_by: User
) -> None:

    dept = selectors.get_department_by_id(
        tenant=tenant,
        department_id=department_id
    )

    if not dept:
        raise ValidationError("Department not found.")

    dept.is_deleted = True
    dept.updated_by = deleted_by
    dept.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
