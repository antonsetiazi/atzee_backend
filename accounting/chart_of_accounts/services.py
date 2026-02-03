# src/accounting/chart_of_accounts/services.py

from typing import Optional
from django.db import transaction
from django.core.exceptions import ValidationError

from accounting.chart_of_accounts.models import ChartOfAccount, AccountType
from accounting.chart_of_accounts import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    """
    Domain rule:
    - None -> ""
    - strip whitespace
    """
    return value.strip() if isinstance(value, str) else ""


def _validate_account_creation(
    *,
    tenant: Tenant,
    code: str,
    parent: Optional[ChartOfAccount],
):
    if selectors.account_code_exists(
        tenant=tenant, code=code
    ):
        raise ValidationError("Account with this code already exists.")
    
    if parent and parent.tenant_id != tenant.id:
        raise ValidationError("Parent account belogns to different tenant.")
    

@transaction.atomic
def create_account(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    account_type: AccountType,
    parent_id: Optional[int] = None,
    is_active: bool = True,
    is_postable: bool = True,
    is_system: bool = False,
) -> ChartOfAccount:
    """
    Create new chart of account.
    """

    name = name.strip()
    code = _normalize_str(code)
    account_type = _normalize_str(account_type)

    parent = None
    
    if parent_id is not None:
        parent_id = int(parent_id)

    if parent_id:
        parent = selectors.get_account_by_id(
            tenant=tenant,
            account_id=parent_id
        )
        if not parent:
            raise ValidationError("Parent account not found.")

    _validate_account_creation(
        tenant=tenant,
        code=code,
        parent=parent,
    )

    account = ChartOfAccount.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        account_type=account_type,
        parent=parent,
        is_active=is_active,
        is_postable=is_postable,
        is_system=is_system,
        created_by=created_by,
    )

    return account


@transaction.atomic
def update_account(
    *,
    tenant: Tenant,
    account_id: int,
    updated_by: User,
    code: str,
    name: str,
    account_type: AccountType,
    parent_id: Optional[int] = None,
    is_active: bool,
    is_postable: bool = True,
    is_system: bool = False,
) -> ChartOfAccount:
    """
    Update existing account.
    """

    account = selectors.get_account_by_id(
        tenant=tenant,
        account_id=account_id
    )

    if not account:
        raise ValidationError("Account not found.")

    name = name.strip()
    code = _normalize_str(code)
    account_type = _normalize_str(account_type)
    
    parent = None
    if parent_id is not None:
        parent_id = int(parent_id)

    if parent_id:
        parent = selectors.get_account_by_id(
            tenant=tenant,
            account_id=parent_id
        )
        if not parent:
            raise ValidationError("Parent account not found.")


    # --- validate ---
    if selectors.account_code_exists(
        tenant=tenant,
        code=code,
        exclude_account_id=account.id,
    ):
        raise ValidationError("Account with this code already exists.")

    if parent and parent.tenant_id != tenant.id:
        raise ValidationError("Parent account belongs to different tenant.")


    # --- apply updates ---
    account.name = name
    account.code = code
    account.account_type = account_type
    account.is_postable = is_postable
    account.is_active = is_active
    account.is_system = is_system
    account.parent = parent   # ✅ boleh None (clear parent)

    account.updated_by = updated_by
    account.save(update_fields=[
        "name",
        "code",
        "parent",
        "account_type",
        "is_postable",
        "is_active",
        "is_system",
        "updated_by",
        "updated_at",
    ])

    return account


@transaction.atomic
def delete_account(
    *,
    tenant: Tenant,
    account_id: int,
    deleted_by: User
) -> None:
    """
    Soft delete account.
    """

    account = selectors.get_account_by_id(
        tenant=tenant,
        account_id=account_id
    )

    if not account:
        raise ValidationError("Account not found.")

    if account.is_system:
        raise ValidationError("System account cannot be deleted.")

    if account.children.exists():
        raise ValidationError("Account has child accounts.")

    account.is_deleted = True
    account.updated_by = deleted_by
    account.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at"
    ])