# core/classifications/tags/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.classifications.tags.models import Tag
from core.classifications.tags import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_uniqueness(*, tenant: Tenant, code: Optional[str], name: Optional[str], exclude_id: Optional[int] = None):
    qs = selectors.get_tag_queryset(tenant=tenant)
    if exclude_id:
        qs = qs.exclude(id=exclude_id)
    if code and qs.filter(code=code).exists():
        raise ValidationError("Tag with this code already exists.")
    if name and qs.filter(name=name).exists():
        raise ValidationError("Tag with this name already exists.")


@transaction.atomic
def create_tag(*, tenant: Tenant, created_by: User, code: str, name: str) -> Tag:
    code = _normalize(code)
    name = _normalize(name)
    _validate_uniqueness(tenant=tenant, code=code, name=name)

    return Tag.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        created_by=created_by,
    )


@transaction.atomic
def update_tag(*, tenant: Tenant, tag_id: int, updated_by: User, code: Optional[str] = None, name: Optional[str] = None, is_active: Optional[bool] = None) -> Tag:
    tag = selectors.get_tag_by_id(tenant=tenant, tag_id=tag_id)
    if not tag:
        raise ValidationError("Tag not found.")

    _validate_uniqueness(tenant=tenant, code=code, name=name, exclude_id=tag.id)

    if code is not None:
        tag.code = _normalize(code)
    if name is not None:
        tag.name = _normalize(name)
    if is_active is not None:
        tag.is_active = is_active

    tag.updated_by = updated_by
    tag.save()

    return tag


@transaction.atomic
def delete_tag(*, tenant: Tenant, tag_id: int, deleted_by: User) -> None:
    tag = selectors.get_tag_by_id(tenant=tenant, tag_id=tag_id)
    if not tag:
        raise ValidationError("Tag not found.")

    tag.is_deleted = True
    tag.updated_by = deleted_by
    tag.save()
