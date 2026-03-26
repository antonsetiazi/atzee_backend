# business/products/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.tenants.models import Tenant
from core.users.models import User
from business.products import selectors
from business.products.models import Product


VALID_PRODUCT_TYPES = {
    Product.TYPE_GOOD,
    Product.TYPE_SERVICE,
}


def _normalize_str(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_product_type(product_type: str):
    if product_type and product_type not in VALID_PRODUCT_TYPES:
        raise ValidationError("Invalid product type.")
    

def _validate_product_uniqueness(
    *,
    tenant: Tenant,
    code: str,
    exclude_product_id: Optional[int] = None
):
    if not code:
        return

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
    name: str,
    code: Optional[str] = None,
    description: Optional[str] = None,
    product_type: Optional[str] = None,
    extensions: Optional[dict] = None,
) -> Product:

    name = name.strip()
    if not name:
        raise ValidationError("Product name is required.")

    code = _normalize_str(code)
    description = _normalize_str(description)
    product_type = _normalize_str(product_type) or Product.TYPE_GOOD

    _validate_product_type(product_type)
    _validate_product_uniqueness(tenant=tenant, code=code)

    return Product.objects.create(
        tenant=tenant,
        name=name,
        code=code or None,
        description=description,
        product_type=product_type,
        extensions=extensions or {},
        created_by=created_by
    )


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
    extensions: Optional[dict] = None,
) -> Product:

    product = selectors.get_product_by_id(
        tenant=tenant,
        product_id=product_id
    )

    if not product:
        raise ValidationError("Product not found.")

    if name is not None:
        name = name.strip()
        if not name:
            raise ValidationError("Product name cannot be empty.")
        product.name = name

    if code is not None:
        code = _normalize_str(code)
        _validate_product_uniqueness(
            tenant=tenant,
            code=code,
            exclude_product_id=product.id
        )
        product.code = code or None

    if description is not None:
        product.description = _normalize_str(description)

    if product_type is not None:
        product_type = _normalize_str(product_type)
        _validate_product_type(product_type)
        product.product_type = product_type

    if extensions is not None:
        product.extensions = extensions

    product.updated_by = updated_by
    product.save()

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