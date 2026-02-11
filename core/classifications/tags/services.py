# core/classifications/tags/services.py

from typing import Optional, Type, Iterable
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError

from core.classifications.tags.models import Tag
from core.classifications.tags import selectors
from core.tenants.models import Tenant
from core.users.models import User

from core.classifications.tags.models import TagRelation

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


@transaction.atomic
def attach_tag(
    *,
    tenant: Tenant,
    obj,
    tag_id: int,
    user: User,
) -> TagRelation:

    tag = selectors.get_tag_by_id(tenant=tenant, tag_id=tag_id)
    if not tag:
        raise ValidationError("Tag not found.")

    content_type = ContentType.objects.get_for_model(obj.__class__)

    relation, created = TagRelation.objects.get_or_create(
        tenant=tenant,
        tag=tag,
        content_type=content_type,
        object_id=obj.id,
        defaults={"created_by": user},
    )

    if not created:
        raise ValidationError("Tag already attached.")

    return relation


@transaction.atomic
def detach_tag(
    *,
    tenant: Tenant,
    obj,
    tag_id: int,
    user: User,
) -> None:

    content_type = ContentType.objects.get_for_model(obj.__class__)

    relation = TagRelation.objects.filter(
        tenant=tenant,
        tag_id=tag_id,
        content_type=content_type,
        object_id=obj.id,
        is_deleted=False,
    ).first()

    if not relation:
        return

    relation.is_deleted = True
    relation.updated_by = user
    relation.save()


@transaction.atomic
def set_tags(
    *,
    tenant: Tenant,
    obj,
    tag_ids: Iterable[int],
    user: User,
) -> None:

    content_type = ContentType.objects.get_for_model(obj.__class__)

    # Soft delete all existing
    TagRelation.objects.filter(
        tenant=tenant,
        content_type=content_type,
        object_id=obj.id,
        is_deleted=False,
    ).update(is_deleted=True, updated_by=user)

    # Attach new
    for tag_id in tag_ids:
        attach_tag(
            tenant=tenant,
            obj=obj,
            tag_id=tag_id,
            user=user,
        )


def get_tags_for_object(
    *,
    tenant: Tenant,
    obj,
) -> QuerySet[Tag]:

    content_type = ContentType.objects.get_for_model(obj.__class__)

    tag_ids = TagRelation.objects.filter(
        tenant=tenant,
        content_type=content_type,
        object_id=obj.id,
        is_deleted=False,
    ).values_list("tag_id", flat=True)

    return Tag.objects.filter(
        tenant=tenant,
        id__in=tag_ids,
        is_deleted=False,
        is_active=True,
    )


def filter_by_tags(
    *,
    tenant: Tenant,
    model_class: Type,
    tag_ids: Iterable[int],
) -> QuerySet:

    content_type = ContentType.objects.get_for_model(model_class)

    object_ids = TagRelation.objects.filter(
        tenant=tenant,
        content_type=content_type,
        tag_id__in=tag_ids,
        is_deleted=False,
    ).values_list("object_id", flat=True)

    return model_class.objects.filter(
        tenant=tenant,
        id__in=object_ids,
        is_deleted=False,
    ).distinct()