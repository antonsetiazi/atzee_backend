from accounting.journals.services import add_journal_line


def build_sales_tax_journal(*, journal, tax, tax_amount):
    """
    Output VAT (utang pajak)
    """
    add_journal_line(
        journal=journal,
        account=tax.sales_account,
        debit=0,
        credit=tax_amount,
        memo=f"Tax {tax.code}"
    )


def build_purchase_tax_journal(*, journal, tax, tax_amount):
    """
    Input VAT (piutang pajak)
    """
    add_journal_line(
        journal=journal,
        account=tax.purchase_account,
        debit=tax_amount,
        credit=0,
        memo=f"Tax {tax.code}"
    )