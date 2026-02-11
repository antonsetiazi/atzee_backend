# core/classifications/attributes/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.classifications.attributes.models.attribute import Attribute
from core.classifications.attributes.models.attribute_option import AttributeOption
from core.tenants.models import Tenant


def get_attribute_queryset(*, tenant: Tenant) -> QuerySet[Attribute]:
    return Attribute.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )


def get_attributes(
    *,
    tenant: Tenant,
    scope: Optional[str] = None,
) -> QuerySet[Attribute]:
    qs = get_attribute_queryset(tenant=tenant)

    if scope:
        qs = qs.filter(scope=scope)

    return qs.filter(is_active=True)


def get_attribute_by_id(
    *,
    tenant: Tenant,
    attribute_id: int,
) -> Optional[Attribute]:
    try:
        return get_attribute_queryset(
            tenant=tenant
        ).get(id=attribute_id)
    except Attribute.DoesNotExist:
        return None


def get_attribute_options(
    *,
    tenant: Tenant,
    attribute: Attribute,
) -> QuerySet[AttributeOption]:
    return AttributeOption.objects.filter(
        tenant=tenant,
        attribute=attribute,
        is_deleted=False,
    )


def get_attribute_option_by_id(
    *,
    tenant: Tenant,
    attribute: Attribute,
    option_id: int,
) -> Optional[AttributeOption]:
    try:
        return get_attribute_options(
            tenant=tenant,
            attribute=attribute,
        ).get(id=option_id)
    except AttributeOption.DoesNotExist:
        return None