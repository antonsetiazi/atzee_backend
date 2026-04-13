# core/fees/services/selectors.py

from core.fees.models import FeeConfig
from core.fees.utils import (
    is_amount_in_range,
    is_category_match,
    is_partner_match,
)

def get_active_fees(tenant_id: str):
    return FeeConfig.objects.filter(
        tenant_id=tenant_id,
        is_active=True
    )

def get_applicable_fees(data):
    qs = FeeConfig.objects.filter(
        tenant_id=data.tenant_id,
        is_active=True
    )

    result = []

    for fee in qs:
        if not is_category_match(fee.category, data.category):
            continue

        if not is_amount_in_range(
            data.amount,
            fee.min_amount,
            fee.max_amount
        ):
            continue

        if not is_partner_match(fee.partner_id, data.partner_id):
            continue

        result.append(fee)

    return result