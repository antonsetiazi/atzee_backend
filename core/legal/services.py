# core/legal/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.legal.models import PolicyDocument, PolicyAcceptance
from core.legal import selectors
from core.tenants.models import Tenant, UserTenant
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_uniqueness(
    *,
    tenant: Tenant,
    code: str,
    version: int,
    exclude_id: Optional[int] = None,
):
    qs = selectors.get_policy_queryset(tenant=tenant)

    if exclude_id:
        qs = qs.exclude(id=exclude_id)

    if qs.filter(code=code, version=version).exists():
        raise ValidationError("Policy version already exists.")


@transaction.atomic
def create_policy(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    title: str,
    policy_type: str,
    content: str,
) -> PolicyDocument:

    code = _normalize(code)
    title = _normalize(title)

    latest = selectors.get_latest_policy(
        tenant=tenant,
        policy_type=policy_type,
    )

    version = 1 if not latest else latest.version + 1

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        version=version,
    )

    return PolicyDocument.objects.create(
        tenant=tenant,
        code=code,
        title=title,
        policy_type=policy_type,
        content=content,
        version=version,
        created_by=created_by,
    )


@transaction.atomic
def update_policy(
    *,
    tenant: Tenant,
    policy_id: int,
    updated_by: User,
    title: Optional[str] = None,
    content: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> PolicyDocument:

    policy = selectors.get_policy_by_id(
        tenant=tenant,
        policy_id=policy_id,
    )

    if not policy:
        raise ValidationError("Policy not found.")

    if title is not None:
        policy.title = _normalize(title)

    if content is not None:
        policy.content = content

    if is_active is not None:
        policy.is_active = is_active

    policy.updated_by = updated_by
    policy.save()

    return policy


@transaction.atomic
def accept_policy(
    *,
    tenant: Tenant,
    user: User,
    policy_id: int,
    ip_address: Optional[str] = None,
) -> PolicyAcceptance:

    policy = selectors.get_policy_by_id(
        tenant=tenant,
        policy_id=policy_id,
    )

    if not policy:
        raise ValidationError("Policy not found.")

    if not UserTenant.objects.filter(
        user=user,
        tenant=tenant,
        is_active=True,
    ).exists():
        raise ValidationError("User is not part of this tenant.")

    if selectors.has_user_accepted_policy(
        user=user,
        policy=policy,
    ):
        raise ValidationError("Policy already accepted.")

    return PolicyAcceptance.objects.create(
        tenant=tenant,
        user=user,
        policy=policy,
        ip_address=ip_address,
        created_by=user,
    )