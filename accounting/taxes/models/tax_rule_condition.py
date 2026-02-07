# accounting/taxes/models/tax_rule_condition.py

from django.db import models
from core.models.base import TenantAwareModel
from .tax_rule import TaxRule


class TaxRuleCondition(TenantAwareModel):
    """
    Atomic condition for tax rule.
    """

    rule = models.ForeignKey(
        TaxRule,
        on_delete=models.CASCADE,
        related_name="conditions"
    )

    field = models.CharField(
        max_length=100,
        help_text="Context path, e.g. customer.is_taxable"
    )

    OPERATOR_CHOICES = (
        ("eq", "Equals"),
        ("neq", "Not equals"),
        ("gt", "Greater than"),
        ("gte", "Greater than or equal"),
        ("lt", "Less than"),
        ("lte", "Less than or equal"),
        ("in", "In"),
    )
    operator = models.CharField(
        max_length=10,
        choices=OPERATOR_CHOICES
    )

    value = models.JSONField()

    class Meta:
        db_table = "accounting_tax_rule_condition"
