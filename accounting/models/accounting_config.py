# accounting/models/accounting_config.py

from django.db import models
import uuid

from core.models.base import (
    TenantAwareModel
)


class AccountingConfig(TenantAwareModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    enforce_credit_limit = models.BooleanField(
        default=True
    )

    allow_over_credit = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "accounting_configs"