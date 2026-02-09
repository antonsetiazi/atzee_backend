# core/classifications/labels/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.classifications.labels.models import Label
from core.classifications.labels import selectors
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
    qs = selectors.get_label_queryset(tenant=tenant)
    if exclude_id:
        qs = qs.exclude(id=exclude_id)

    if code and qs.filter(code=code).exists():
        raise ValidationError("Label with this code already exists.")
    if scope and name and qs.filter(scope=scope, name=name).exists():
        raise ValidationError("Label with this name already exists in this scope.")


@transaction.atomic
def create_label(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    scope: str,
    description: Optional[str] = "",
) -> Label:

    code = _normalize(code)
    name = _normalize(name)
    scope = _normalize(scope)
    description = _normalize(description)

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        scope=scope,
        name=name,
    )

    return Label.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        scope=scope,
        description=description,
        created_by=created_by,
    )


@transaction.atomic
def update_label(
    *,
    tenant: Tenant,
    label_id: int,
    updated_by: User,
    code: Optional[str] = None,
    name: Optional[str] = None,
    scope: Optional[str] = None,
    description: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Label:

    label = selectors.get_label_by_id(tenant=tenant, label_id=label_id)
    if not label:
        raise ValidationError("Label not found.")

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        scope=scope or label.scope,
        name=name,
        exclude_id=label.id,
    )

    if code is not None:
        label.code = _normalize(code)
    if name is not None:
        label.name = _normalize(name)
    if scope is not None:
        label.scope = _normalize(scope)
    if description is not None:
        label.description = _normalize(description)
    if is_active is not None:
        label.is_active = is_active

    label.updated_by = updated_by
    label.save()

    return label


@transaction.atomic
def delete_label(
    *,
    tenant: Tenant,
    label_id: int,
    deleted_by: User,
) -> None:
    label = selectors.get_label_by_id(tenant=tenant, label_id=label_id)
    if not label:
        raise ValidationError("Label not found.")

    label.is_deleted = True
    label.updated_by = deleted_by
    label.save()
