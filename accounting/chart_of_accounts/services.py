from typing import Optional
from django.db import transaction
from django.core.exceptions import ValidationError

from accounting.chart_of_accounts.models import ChartOfAccount, AccountType
from accounting.chart_of_accounts import selectors
from core.tenants.models import Tenant
from core.users.models import User


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
    is_postable: bool = True,
    is_system: bool = False,
) -> ChartOfAccount:
    """
    Create new chart of account.
    """

    parent = None
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
        is_postable=is_postable,
        is_system=is_system,
        created_by=created_by,
    )

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