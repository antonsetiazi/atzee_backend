# core/classifications/attributes/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.classifications.attributes.models.attribute import Attribute
from core.classifications.attributes.models.attribute_option import AttributeOption
from core.classifications.attributes import selectors
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
    qs = selectors.get_attribute_queryset(tenant=tenant)

    if exclude_id:
        qs = qs.exclude(id=exclude_id)

    if code and qs.filter(code=code).exists():
        raise ValidationError("Attribute with this code already exists.")

    if scope and name and qs.filter(scope=scope, name=name).exists():
        raise ValidationError("Attribute with this name already exists in this scope.")


@transaction.atomic
def create_attribute(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    type: str,
    scope: str,
) -> Attribute:

    code = _normalize(code)
    name = _normalize(name)
    scope = _normalize(scope)

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        scope=scope,
        name=name,
    )

    return Attribute.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        type=type,
        scope=scope,
        created_by=created_by,
    )


@transaction.atomic
def update_attribute(
    *,
    tenant: Tenant,
    attribute_id: int,
    updated_by: User,
    code: Optional[str] = None,
    name: Optional[str] = None,
    type: Optional[str] = None,
    scope: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Attribute:

    attribute = selectors.get_attribute_by_id(
        tenant=tenant,
        attribute_id=attribute_id,
    )

    if not attribute:
        raise ValidationError("Attribute not found.")

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        scope=scope or attribute.scope,
        name=name,
        exclude_id=attribute.id,
    )

    if code is not None:
        attribute.code = _normalize(code)
    if name is not None:
        attribute.name = _normalize(name)
    if type is not None:
        attribute.type = type
    if scope is not None:
        attribute.scope = _normalize(scope)
    if is_active is not None:
        attribute.is_active = is_active

    attribute.updated_by = updated_by
    attribute.save()

    return attribute


@transaction.atomic
def delete_attribute(
    *,
    tenant: Tenant,
    attribute_id: int,
    deleted_by: User,
) -> None:

    attribute = selectors.get_attribute_by_id(
        tenant=tenant,
        attribute_id=attribute_id,
    )

    if not attribute:
        raise ValidationError("Attribute not found.")

    attribute.is_deleted = True
    attribute.updated_by = deleted_by
    attribute.save()


def _validate_option_uniqueness(
    *,
    tenant: Tenant,
    attribute: Attribute,
    code: Optional[str],
    name: Optional[str],
    exclude_id: Optional[int] = None,
) -> None:
    qs = AttributeOption.objects.filter(
        tenant=tenant,
        attribute=attribute,
        is_deleted=False,
    )

    if exclude_id:
        qs = qs.exclude(id=exclude_id)

    if code and qs.filter(code=code).exists():
        raise ValidationError("Option with this code already exists.")

    if name and qs.filter(name=name).exists():
        raise ValidationError("Option with this name already exists.")


@transaction.atomic
def create_attribute_option(
    *,
    tenant: Tenant,
    attribute: Attribute,
    created_by: User,
    code: str,
    name: str,
) -> AttributeOption:

    code = _normalize(code)
    name = _normalize(name)

    _validate_option_uniqueness(
        tenant=tenant,
        attribute=attribute,
        code=code,
        name=name,
    )

    return AttributeOption.objects.create(
        tenant=tenant,
        attribute=attribute,
        code=code,
        name=name,
        created_by=created_by,
    )


@transaction.atomic
def update_attribute_option(
    *,
    tenant: Tenant,
    attribute: Attribute,
    option_id: int,
    updated_by: User,
    code: Optional[str] = None,
    name: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> AttributeOption:

    option = selectors.get_attribute_option_by_id(
        tenant=tenant,
        attribute=attribute,
        option_id=option_id,
    )

    if not option:
        raise ValidationError("Attribute option not found.")

    _validate_option_uniqueness(
        tenant=tenant,
        attribute=attribute,
        code=code,
        name=name,
        exclude_id=option.id,
    )

    if code is not None:
        option.code = _normalize(code)
    if name is not None:
        option.name = _normalize(name)
    if is_active is not None:
        option.is_active = is_active

    option.updated_by = updated_by
    option.save()

    return option


@transaction.atomic
def delete_attribute_option(
    *,
    tenant: Tenant,
    attribute: Attribute,
    option_id: int,
    deleted_by: User,
) -> None:

    option = selectors.get_attribute_option_by_id(
        tenant=tenant,
        attribute=attribute,
        option_id=option_id,
    )

    if not option:
        raise ValidationError("Attribute option not found.")

    option.is_deleted = True
    option.updated_by = deleted_by
    option.save()