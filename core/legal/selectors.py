# core/legal/selectors.py

from typing import Optional
from django.db.models import QuerySet, Max
from core.legal.models import PolicyDocument, PolicyAcceptance
from core.tenants.models import Tenant
from core.users.models import User


def get_policy_queryset(*, tenant: Tenant) -> QuerySet[PolicyDocument]:
    return PolicyDocument.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )


def get_policies(
    *,
    tenant: Tenant,
    policy_type: Optional[str] = None,
) -> QuerySet[PolicyDocument]:
    qs = get_policy_queryset(tenant=tenant)

    if policy_type:
        qs = qs.filter(policy_type=policy_type)

    return qs.filter(is_active=True)


def get_latest_policy(
    *,
    tenant: Tenant,
    policy_type: str,
) -> Optional[PolicyDocument]:
    qs = get_policy_queryset(
        tenant=tenant
    ).filter(
        policy_type=policy_type,
        is_active=True,
    )

    return qs.order_by("-version").first()


def get_policy_by_id(
    *,
    tenant: Tenant,
    policy_id: int,
) -> Optional[PolicyDocument]:
    try:
        return get_policy_queryset(
            tenant=tenant
        ).get(id=policy_id)
    except PolicyDocument.DoesNotExist:
        return None


def has_user_accepted_policy(
    *,
    user: User,
    policy: PolicyDocument,
) -> bool:
    return PolicyAcceptance.objects.filter(
        user=user,
        policy=policy,
    ).exists()


def get_unaccepted_policies(*, tenant, user):
    policies = get_policies(tenant=tenant)

    return [
        p for p in policies
        if not has_user_accepted_policy(user=user, policy=p)
    ]