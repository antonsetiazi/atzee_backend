# accounting/journals/contributors/tax.py

from decimal import Decimal
from accounting.taxes.services.tax_engine import TaxEngine
from accounting.journals.services import add_journal_line
from accounting.journals.constants import JournalType


class TaxJournalContributor:
    """
    Inject tax journal lines into a draft journal.
    """

    @staticmethod
    def apply(
        *,
        journal,
        base_amount: Decimal,
        context: dict,
    ):
        """
        Adds tax lines to a draft journal.
        """

        if journal.status != "DRAFT":
            return

        # Map JournalType → tax event
        if journal.journal_type == JournalType.SALES:
            event = "sales"
        elif journal.journal_type == JournalType.PURCHASE:
            event = "purchase"
        else:
            return  # journal type not taxable

        tax_result = TaxEngine.compute(
            tenant=journal.tenant,
            base_amount=base_amount,
            journal_type=event,
            at_date=journal.journal_date,
            context=context,
        )

        if not tax_result:
            return

        add_journal_line(
            journal=journal,
            account=tax_result["debit_account"],
            debit=tax_result["tax_amount"],
            memo=f"Tax {tax_result['tax'].code}"
        )

        add_journal_line(
            journal=journal,
            account=tax_result["credit_account"],
            credit=tax_result["tax_amount"],
            memo=f"Tax {tax_result['tax'].code}"
        )
