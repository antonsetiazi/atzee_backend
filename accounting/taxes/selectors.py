from core.tenants.models import Tenant
from accounting.taxes.models import Tax
from datetime import date


def get_applicable_tax(
    *, 
    tenant: Tenant,
    code: str,
    at_date: date
) -> Tax | None:
    return (
        Tax.objects
        .filter(
            tenant=tenant,
            code=code,
            effective_from__lte=at_date,
            is_active=True
        )
        .filter(
            effective_to__isnull=True
        )
        .order_by("-effective_from")
        .first()
    )