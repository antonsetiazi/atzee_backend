# business/transactions/reference_generators/sales.py

from django.utils import timezone
from django.db.models import Max

from business.transactions.models.transaction import Transaction


def generate_sales_reference(tenant):

    today = timezone.now()
    prefix = f"SLS-{today:%Y%m}"

    last_ref = (
        Transaction.objects
        .filter(
            tenant=tenant,
            reference__startswith=prefix,
        )
        .aggregate(max_ref=Max("reference"))
        .get("max_ref")
    )

    if not last_ref:
        next_number = 1
    else:
        next_number = int(last_ref.split("-")[-1]) + 1

    return f"{prefix}-{next_number:04d}"