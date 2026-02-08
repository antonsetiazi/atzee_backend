# core.master/uom/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.master.uom.models import UOM
from core.master.uom import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    """
    Domain rule:
    - None -> ""
    - strip whitespace
    """
    return value.strip() if isinstance(value, str) else ""


def _validate_uom_uniqueness(
        *, 
        tenant: Tenant,
        symbol: Optional[str],
        exclude_uom_id: Optional[int] = None
) -> None:
    """
    Prevent duplicate uom by symbol within tenant.
    """

    qs = selectors.get_uom_queryset(tenant=tenant)

    if exclude_uom_id:
        qs = qs.exclude(id=exclude_uom_id)
    
    if symbol and qs.filter(symbol=symbol).exists():
        raise ValidationError("UOM with this symbol already exists.")
    

@transaction.atomic
def create_uom(
    *,
    tenant: Tenant,
    created_by: User,
    name: str,
    code: Optional[str] = None,
    symbol: Optional[str] = None,
    category_id: Optional[int] = None,
    is_base: bool = True,
    precision: int = 2,
) -> UOM:
    """
    Create new uom.
    """
    # ✅ DOMAIN NORMALIZATION
    name = name.strip()
    code = _normalize_str(code)
    symbol = _normalize_str(symbol)

    category = None

    if category_id is not None:
        category_id = int(category_id)
    
    if category_id:
        category = selectors.get_category_by_id(
            tenant=tenant,
            category_id=category_id
        )
        if not category:
            raise ValidationError("Category not found.")
    
    if not precision:
        precision = 2
        
    # ✅ DOMAIN VALIDATION
    _validate_uom_uniqueness(
        tenant=tenant,
        symbol=symbol or None
    )

    uom = UOM.objects.create(
        tenant=tenant,
        name=name,
        code=code,
        symbol=symbol,
        category=category,
        is_base=is_base,
        precision=precision,
        created_by=created_by
    )

    return uom


@transaction.atomic
def update_uom(
    *,
    tenant: Tenant,
    uom_id: int,
    updated_by: User,
    name: Optional[str] = None,
    code: Optional[str] = None,
    symbol: Optional[str] = None,
    category_id: Optional[int] = None,
    is_base: bool = None,
    precision: Optional[int] = 2,
) -> UOM:
    """
    Update existing uom.
    """

    uom = selectors.get_uom_by_id(
        tenant=tenant,
        uom_id=uom_id
    )

    if not uom:
        raise ValidationError("UOM not found.")
    
    category = None

    if category_id is not None:
        category_id = int(category_id)
    
    if category_id:
        category = selectors.get_category_by_id(
            tenant=tenant,
            category_id=category_id
        )
        if not category:
            raise ValidationError("Category not found.")
        
    _validate_uom_uniqueness(
        tenant=tenant,
        symbol=symbol,
        exclude_uom_id=uom.id
    )

    if name is not None:
        uom.name = name
    if code is not None:
        uom.code = code
    if symbol is not None:
        uom.symbol = symbol
    if category is not None:
        uom.category = category
    if is_base is not None:
        uom.is_base = is_base
    if precision is not None:
        uom.precision = precision

    uom.updated_by = updated_by
    uom.save(update_fields=[
        "name",
        "code",
        "symbol",
        "category",
        "is_base",
        "precision",
        "updated_by",
        "updated_at"
    ])

    return uom


@transaction.atomic
def delete_uom(
    *,
    tenant: Tenant,
    uom_id: int,
    deleted_by: User
) -> None:
    """
    Soft delete uom.
    """
    
    uom = selectors.get_uom_by_id(
        tenant=tenant,
        uom_id=uom_id
    )
    
    if not uom:
        raise ValidationError("UOM not found")

    uom.is_deleted = True
    uom.updated_by = deleted_by
    uom.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])