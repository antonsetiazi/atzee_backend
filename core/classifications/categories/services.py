# core/classifications/categories/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.classifications.categories.models import Category
from core.classifications.categories import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_uniqueness(
    *,
    tenant: Tenant,
    code: Optional[str],
    scope: Optional[str],
    name: Optional[str],
    exclude_id: Optional[int] = None,
) -> None:
    qs = selectors.get_category_queryset(tenant=tenant)

    if exclude_id:
        qs = qs.exclude(id=exclude_id)

    if code and qs.filter(code=code).exists():
        raise ValidationError("Category with this code already exists.")

    if scope and name and qs.filter(scope=scope, name=name).exists():
        raise ValidationError("Category with this name already exists in this scope.")


@transaction.atomic
def create_category(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    scope: str,
    parent_id: Optional[int] = None,
) -> Category:

    code = _normalize(code)
    name = _normalize(name)
    scope = _normalize(scope)

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        scope=scope,
        name=name,
    )

    parent = None
    if parent_id:
        parent = selectors.get_category_by_id(
            tenant=tenant,
            category_id=parent_id,
        )
        if not parent:
            raise ValidationError("Parent category not found.")

    return Category.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        scope=scope,
        parent=parent,
        created_by=created_by,
    )


@transaction.atomic
def update_category(
    *,
    tenant: Tenant,
    category_id: int,
    updated_by: User,
    code: Optional[str] = None,
    name: Optional[str] = None,
    scope: Optional[str] = None,
    parent_id: Optional[int] = None,
    is_active: Optional[bool] = None,
) -> Category:

    category = selectors.get_category_by_id(
        tenant=tenant,
        category_id=category_id,
    )

    if not category:
        raise ValidationError("Category not found.")

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        scope=scope or category.scope,
        name=name,
        exclude_id=category.id,
    )

    if code is not None:
        category.code = _normalize(code)
    if name is not None:
        category.name = _normalize(name)
    if scope is not None:
        category.scope = _normalize(scope)
    if parent_id is not None:
        if parent_id == category.id:
            raise ValidationError("Category cannot be its own parent.")

        if parent_id:
            parent = selectors.get_category_by_id(
                tenant=tenant,
                category_id=parent_id,
            )
            if not parent:
                raise ValidationError("Parent category not found.")
            category.parent = parent
        else:
            category.parent = None

    if is_active is not None:
        category.is_active = is_active

    category.updated_by = updated_by
    category.save()

    return category


@transaction.atomic
def delete_category(
    *,
    tenant: Tenant,
    category_id: int,
    deleted_by: User,
) -> None:

    category = selectors.get_category_by_id(
        tenant=tenant,
        category_id=category_id,
    )

    if not category:
        raise ValidationError("Category not found.")

    if category.children.filter(is_deleted=False).exists():
        raise ValidationError("Cannot delete category with children.")

    category.is_deleted = True
    category.updated_by = deleted_by
    category.save()
