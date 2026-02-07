# accounting/taxes/services/tax_resolver.py

from datetime import date
from accounting.taxes.models import Tax, TaxRate, TaxRule
from .tax_rule_evaluator import TaxRuleEvaluator


class TaxResolver:
    @staticmethod
    def resolve_tax(
        *,
        tenant,
        event: str,          # "sales" | "purchase"
        at_date: date,
        context: dict,
    ) -> tuple[Tax, TaxRate] | None:
        """
        Resolve tax via rules + rate.
        """

        rules = (
            TaxRule.objects
            .filter(
                tenant=tenant,
                event=event,
                is_active=True,
                tax__is_active=True,
            )
            .select_related("tax")
            .prefetch_related("conditions")
        )

        for rule in rules:
            if TaxRuleEvaluator.evaluate(rule, context):
                tax = rule.tax
                rate = (
                    TaxRate.objects
                    .filter(
                        tenant=tenant,
                        tax=tax,
                        effective_from__lte=at_date,
                    )
                    .filter(
                        effective_to__isnull=True
                    )
                    .order_by("-effective_from")
                    .first()
                )

                if rate:
                    return tax, rate

        return None
