# core/schedule/services/recurring_service.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.schedule.recurring.models import RecurringRule
from core.schedule.recurring import selectors
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_recurring_rule(
    *,
    tenant: Tenant,
    created_by: User,
    event_id: int,
    rrule: str,
    end_date=None,
    exceptions: Optional[list] = None
) -> RecurringRule:

    rule = RecurringRule.objects.create(
        tenant=tenant,
        created_by=created_by,
        event_id=event_id,
        rrule=rrule,
        end_date=end_date,
        exceptions=exceptions or []
    )
    return rule


@transaction.atomic
def update_recurring_rule(
    *,
    tenant: Tenant,
    rule_id: int,
    updated_by: User,
    rrule: Optional[str] = None,
    end_date=None,
    exceptions: Optional[list] = None
) -> RecurringRule:

    rule = selectors.get_recurring_rule_by_id(tenant=tenant, rule_id=rule_id)
    if not rule:
        raise ValidationError("Recurring rule not found.")

    if rrule is not None:
        rule.rrule = rrule
    if end_date is not None:
        rule.end_date = end_date
    if exceptions is not None:
        rule.exceptions = exceptions

    rule.updated_by = updated_by
    rule.save(update_fields=["rrule", "end_date", "exceptions", "updated_by", "updated_at"])
    return rule


@transaction.atomic
def delete_recurring_rule(*, tenant: Tenant, rule_id: int, deleted_by: User):
    rule = selectors.get_recurring_rule_by_id(tenant=tenant, rule_id=rule_id)
    if not rule:
        raise ValidationError("Recurring rule not found.")

    rule.is_deleted = True
    rule.updated_by = deleted_by
    rule.save(update_fields=["is_deleted", "updated_by", "updated_at"])
