from typing import Optional
from uuid import UUID

from django.db import transaction
from django.core.exceptions import ValidationError

from hr.employees.models import Employee
from hr.employees import selectors
from hr.employees.gateways import user_gateway

from core.tenants.models import Tenant
from core.users.models import User


def _validate_employee_uniqueness(
    *,
    tenant: Tenant,
    user_id: UUID,
    employee_code: Optional[str],
    exclude_employee_id: Optional[int] = None
) -> None:
    qs = selectors.get_employee_queryset(
        tenant=tenant
    )

    if exclude_employee_id:
        qs = qs.exclude(id=exclude_employee_id)

    if qs.filter(user_id=user_id).exists():
        raise ValidationError(
            "Employee already exists for this user."
        )
    
    if employee_code and qs.filter(
        employee_code=employee_code
    ).exists():
        raise ValidationError(
            "Employee code already exists."
        )
    

@transaction.atomic
def create_employee(
    *,
    tenant: Tenant,
    created_by: User,
    user_id: UUID,
    full_name: str,
    join_date,
    employee_code: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    job_title: Optional[str] = None,
    notes: Optional[str] = None
) -> Employee:
    
    # Validate Core User
    user_gateway.ensure_user_is_active(
        user_id=user_id
    )

    _validate_employee_uniqueness(
        tenant=tenant,
        user_id=user_id,
        employee_code=employee_code
    )

    employee = Employee.objects.create(
        tenant=tenant,
        user_id=user_id,
        full_name=full_name,
        join_date=join_date,
        employee_code=employee_code,
        email=email,
        phone=phone,
        job_title=job_title,
        notes=notes,
        created_by=created_by
    )

    return employee


@transaction.atomic
def update_employee(
    *,
    tenant: Tenant,
    employee_id: int,
    updated_by: User,
    full_name: Optional[str] = None,
    employee_code: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    job_title: Optional[str] = None,
    is_active: Optional[bool] = None,
    notes: Optional[str] = None
) -> Employee:
    
    employee = selectors.get_employee_by_id(
        tenant=tenant,
        employee_id=employee_id
    )

    if not employee:
        raise ValidationError("Employee not found.")
    
    if employee_code or employee.user_id:
        _validate_employee_uniqueness(
            tenant=tenant,
            user_id=employee.user_id,
            employee_code=employee_code,
            exclude_employee_id=employee.id
        )

    if full_name is not None:
        employee.full_name = full_name
    if employee_code is not None:
        employee.employee_code = employee_code
    if email is not None:
        employee.email = email
    if phone is not None:
        employee.phone = phone
    if job_title is not None:
        employee.job_title = job_title
    if is_active is not None:
        employee.is_active = is_active
    if notes is not None:
        employee.notes = notes

    employee.updated_by = updated_by
    employee.save(update_fields=[
        "full_name",
        "employee_code",
        "email",
        "phone",
        "job_title",
        "is_active",
        "notes",
        "updated_by",
        "updated_at"
    ])

    return employee


@transaction.atomic
def delete_employee(
    *,
    tenant: Tenant,
    employee_id: int,
    deleted_by: User
) -> None:
    
    employee = selectors.get_employee_by_id(
        tenant=tenant,
        employee_id=employee_id
    )

    if not employee:
        raise ValidationError("Employee not found.")

    employee.is_deleted = True
    employee.updated_by = deleted_by
    employee.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at"
    ])
