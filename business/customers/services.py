# business/customers/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from business.customers.models import Customer
from business.customers import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    """
    Domain rule:
    - None -> ""
    - strip whitespace
    """
    return value.strip() if isinstance(value, str) else ""


def _validate_customer_uniqueness(
        *, 
        tenant: Tenant,
        email: Optional[str],
        phone: Optional[str],
        exclude_customer_id: Optional[int] = None
) -> None:
    """
    Prevent duplicate customer by email or phone within tenant.
    """

    qs = selectors.get_customer_queryset(tenant=tenant)

    if exclude_customer_id:
        qs = qs.exclude(id=exclude_customer_id)
    
    if email and qs.filter(email=email).exists():
        raise ValidationError("Customer with this email already exists.")
    
    if phone and qs.filter(phone=phone).exists():
        raise ValidationError("Customer with this phone already exists.")
    

@transaction.atomic
def create_customer(
    *,
    tenant: Tenant,
    created_by: User,
    name: str,
    code: Optional[str] = None,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    address: Optional[str] = None,
    notes: Optional[str] = None
) -> Customer:
    """
    Create new customer.
    """

    # ✅ DOMAIN NORMALIZATION
    name = name.strip()
    code = _normalize_str(code)
    phone = _normalize_str(phone)
    email = _normalize_str(email)
    address = _normalize_str(address)
    notes = _normalize_str(notes)

    # ✅ DOMAIN VALIDATION
    _validate_customer_uniqueness(
        tenant=tenant,
        email=email or None,
        phone=phone or None
    )

    customer = Customer.objects.create(
        tenant=tenant,
        name=name,
        code=code,
        phone=phone,
        email=email,
        address=address,
        notes=notes,
        created_by=created_by
    )

    return customer


@transaction.atomic
def update_customer(
    *,
    tenant: Tenant,
    customer_id: int,
    updated_by: User,
    name: Optional[str] = None,
    code: Optional[str] = None,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    address: Optional[str] = None,
    notes: Optional[str] = None
) -> Customer:
    """
    Update existing customer.
    """

    customer = selectors.get_customer_by_id(
        tenant=tenant,
        customer_id=customer_id
    )

    if not customer:
        raise ValidationError("Customer not found.")
    
    _validate_customer_uniqueness(
        tenant=tenant,
        email=email,
        phone=phone,
        exclude_customer_id=customer.id
    )

    if name is not None:
        customer.name = name
    if code is not None:
        customer.code = code
    if phone is not None:
        customer.phone = phone
    if email is not None:
        customer.email = email
    if address is not None:
        customer.address = address
    if notes is not None:
        customer.notes = notes

    customer.updated_by = updated_by
    customer.save(update_fields=[
        "name",
        "code",
        "phone",
        "email",
        "address",
        "notes",
        "updated_by",
        "updated_at"
    ])

    return customer


@transaction.atomic
def delete_customer(
    *,
    tenant: Tenant,
    customer_id: int,
    deleted_by: User
) -> None:
    """
    Soft delete customer.
    """
    
    customer = selectors.get_customer_by_id(
        tenant=tenant,
        customer_id=customer_id
    )
    
    if not customer:
        raise ValidationError("Customer not found")

    customer.is_deleted = True
    customer.updated_by = deleted_by
    customer.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])