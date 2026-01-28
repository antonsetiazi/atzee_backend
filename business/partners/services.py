from typing import Optional
from django.db import transaction
from django.core.exceptions import ValidationError

from business.partners.models import Partner
from business.partners import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    """
    Domain rule:
    - None -> ""
    - strip whitespace
    """
    return value.strip() if isinstance(value, str) else ""


def _validate_partner_uniqueness(
        *, 
        tenant: Tenant,
        email: Optional[str],
        phone: Optional[str],
        exclude_partner_id: Optional[int] = None
) -> None:
    """
    Prevent duplicate partner by email or phone within tenant.
    """

    qs = selectors.get_partner_queryset(tenant=tenant)

    if exclude_partner_id:
        qs = qs.exclude(id=exclude_partner_id)
    
    if email and qs.filter(email=email).exists():
        raise ValidationError("Partner with this email already exists.")
    
    if phone and qs.filter(phone=phone).exists():
        raise ValidationError("Partner with this phone already exists.")
    

@transaction.atomic
def create_partner(
    *,
    tenant: Tenant,
    created_by: User,
    name: str,
    code: Optional[str] = None,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    address: Optional[str] = None,
    notes: Optional[str] = None
) -> Partner:
    """
    Create new partner.
    """

    # ✅ DOMAIN NORMALIZATION
    name = name.strip()
    code = _normalize_str(code)
    phone = _normalize_str(phone)
    email = _normalize_str(email)
    address = _normalize_str(address)
    notes = _normalize_str(notes)

    _validate_partner_uniqueness(
        tenant=tenant,
        email=email or None,
        phone=phone or None
    )

    partner = Partner.objects.create(
        tenant=tenant,
        name=name,
        code=code,
        phone=phone,
        email=email,
        address=address,
        notes=notes,
        created_by=created_by
    )

    return partner


@transaction.atomic
def update_partner(
    *,
    tenant: Tenant,
    partner_id: int,
    updated_by: User,
    name: Optional[str] = None,
    code: Optional[str] = None,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    address: Optional[str] = None,
    notes: Optional[str] = None
) -> Partner:
    """
    Update existing partner.
    """

    partner = selectors.get_partner_by_id(
        tenant=tenant,
        partner_id=partner_id
    )

    if not partner:
        raise ValidationError("Partner not found.")
    
    _validate_partner_uniqueness(
        tenant=tenant,
        email=email,
        phone=phone,
        exclude_partner_id=partner.id
    )

    if name is not None:
        partner.name = name
    if code is not None:
        partner.code = code
    if phone is not None:
        partner.phone = phone
    if email is not None:
        partner.email = email
    if address is not None:
        partner.address = address
    if notes is not None:
        partner.notes = notes

    partner.updated_by = updated_by
    partner.save(update_fields=[
        "name",
        "code",
        "phone",
        "email",
        "address",
        "notes",
        "updated_by",
        "updated_at"
    ])

    return partner


@transaction.atomic
def delete_partner(
    *,
    tenant: Tenant,
    partner_id: int,
    deleted_by: User
) -> None:
    """
    Soft delete partner.
    """

    partner = selectors.get_partner_by_id(
        tenant=tenant,
        partner_id=partner_id
    )

    if not partner:
        raise ValidationError("Partner not found")
    
    partner.is_deleted = True
    partner.updated_by = deleted_by
    partner.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])