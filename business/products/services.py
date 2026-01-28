# business/products/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.tenants.models import Tenant
from core.users.models import User
from business.products import selectors
from business.products.models import Product


def _normalize_str(value: Optional[str]) -> str:
    """
    Domain rule:
    - None -> ""
    - strip whitespace
    """
    return value.strip() if isinstance(value, str) else ""


def _validate_product_uniqueness(
        *, 
        tenant: Tenant,
        code: str,
        exclude_product_id: Optional[int] = None
) -> None:
    qs = selectors.get_product_queryset(tenant=tenant).filter(code=code)

    if exclude_product_id:
        qs = qs.exclude(id=exclude_product_id)
    
    if qs.exists():
        raise ValidationError("Product code already exists.")
    

@transaction.atomic
def create_product(
    *,
    tenant: Tenant,
    created_by: User,
    name: Optional[str],
    code: Optional[str],
    description: Optional[str] = None,
    product_type: Optional[str] = None,
) -> Product:
    """
    Create new product.
    """

    # ✅ DOMAIN NORMALIZATION
    name = name.strip()
    code = _normalize_str(code)
    description = _normalize_str(description)
    product_type = _normalize_str(product_type)

    _validate_product_uniqueness(
        tenant=tenant,
        code=code,
    )

    product = Product.objects.create(
        tenant=tenant,
        name=name,
        code=code,
        description=description,
        product_type=product_type,
        created_by=created_by
    )

    return product


@transaction.atomic
def update_product(
    *,
    tenant: Tenant,
    product_id: int,
    updated_by: User,
    name: Optional[str] = None,
    code: Optional[str] = None,
    description: Optional[str] = None,
    product_type: Optional[str] = None,
) -> Product:
    """
    Update existing product.
    """

    product = selectors.get_product_by_id(
        tenant=tenant,
        product_id=product_id
    )

    if not product:
        raise ValidationError("Product not found.")
    
    _validate_product_uniqueness(
        tenant=tenant,
        code=code,
        exclude_product_id=product.id
    )

    if name is not None:
        product.name = name
    if code is not None:
        product.code = code
    if description is not None:
        product.description = description
    if product_type is not None:
        product.product_type = product_type

    product.updated_by = updated_by
    product.save(update_fields=[
        "name",
        "code",
        "description",
        "product_type",
        "updated_by",
        "updated_at"
    ])

    return product


@transaction.atomic
def delete_product(
    *,
    tenant: Tenant,
    product_id: int,
    deleted_by: User
) -> None:
    """
    Soft delete product.
    """

    product = selectors.get_product_by_id(
        tenant=tenant,
        product_id=product_id
    )

    if not product:
        raise ValidationError("Product not found")
    
    product.is_deleted = True
    product.updated_by = deleted_by
    product.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])


@transaction.atomic
def set_product_active_status(
    *,
    tenant: Tenant,
    user: User,
    product_id: int,
    is_active: bool
) -> Product:
    """
    Activate or deactivate product.
    """

    product = selectors.get_product_by_id(
        tenant=tenant,
        product_id=product_id
    )

    if not product:
        raise ValidationError("Product not found.")
    
    product.is_active = is_active
    product.updated_by = user
    product.save(update_fields=[
        "is_active",
        "updated_by",
        "updated_at",
    ])

    return product