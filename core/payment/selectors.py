# core/payment/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.payment.models import Payment, PaymentMethod
from core.tenants.models import Tenant
from core.users.models import User


def get_payment_queryset(*, tenant) -> QuerySet[Payment]:
    return Payment.objects.filter(tenant=tenant, is_deleted=False)


def get_payments_by_user(*, tenant, user: User) -> QuerySet[Payment]:
    return get_payment_queryset(tenant=tenant).filter(user=user)


def get_payment_by_id(*, tenant, payment_id: int) -> Optional[Payment]:
    try:
        return get_payment_queryset(tenant=tenant).get(id=payment_id)
    except Payment.DoesNotExist:
        return None


def get_payment_method_by_code(*, tenant, code: str) -> Optional[PaymentMethod]:
    try:
        return PaymentMethod.objects.get(tenant=tenant, code=code, is_deleted=False, is_active=True)
    except PaymentMethod.DoesNotExist:
        return None