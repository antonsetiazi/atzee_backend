# accounting/taxes/services/tax_engine.py

from datetime import date
from decimal import Decimal
from accounting.taxes.models import TaxJournalMap
from .tax_resolver import TaxResolver
from .tax_calculator import TaxCalculator


class TaxEngine:
    """
    Core tax computation engine.
    """

    @staticmethod
    def compute(
        *,
        tenant,
        base_amount: Decimal,
        journal_type: str,   # "sales" | "purchase"
        at_date: date,
        context,
    ) -> dict | None:
        """
        Compute tax and prepare journal mapping.
        """

        resolved = TaxResolver.resolve_tax(
            tenant=tenant,
            event=journal_type,
            at_date=at_date,
            context=context,
        )

        if not resolved:
            return None

        tax, rate = resolved

        # Validate scope
        if tax.scope not in (journal_type, "both"):
            return None

        tax_amount = TaxCalculator.calculate(
            tax=tax,
            base_amount=base_amount,
            rate=rate.rate,
        )

        journal_map = (
            TaxJournalMap.objects
            .filter(
                tenant=tenant,
                tax=tax,
                journal_type=journal_type,
            )
            .first()
        )

        if not journal_map:
            raise RuntimeError(
                f"No journal map for tax {tax.code} ({journal_type})"
            )

        return {
            "tax": tax,
            "rate": rate.rate,
            "base_amount": base_amount,
            "tax_amount": tax_amount,
            "journal_type": journal_type,
            "debit_account": journal_map.debit_account,
            "credit_account": journal_map.credit_account,
        }
