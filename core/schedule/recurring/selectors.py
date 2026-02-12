# core/schedule/recurring/selectors.py

from typing import Optional
from core.schedule.recurring.models import RecurringRule
from core.tenants.models import Tenant


def get_recurring_rule_queryset(*, tenant: Tenant):
    return RecurringRule.objects.filter(tenant=tenant, is_deleted=False)


def get_recurring_rule_by_id(*, tenant: Tenant, rule_id: int) -> Optional[RecurringRule]:
    try:
        return RecurringRule.objects.get(tenant=tenant, id=rule_id, is_deleted=False)
    except RecurringRule.DoesNotExist:
        return None
