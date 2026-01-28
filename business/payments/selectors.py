from typing import Optional
from django.db.models import QuerySet

from business.payments.models import Payment
from core.tenants.models import Tenant


def get_payment_queryset(*, tenant: Tenant) -> QuerySet[Payment]:
    return Payment.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_payments(*, tenant: Tenant) -> QuerySet[Payment]:
    return (
        get_payment_queryset(tenant=tenant)
        .order_by("-payment_date", "-id")
    )


def get_payment_by_id(
    *,
    tenant: Tenant,
    payment_id: int
) -> Optional[Payment]:
    try:
        return get_payment_queryset(tenant=tenant).get(id=payment_id)
    except Payment.DoesNotExist:
        return None