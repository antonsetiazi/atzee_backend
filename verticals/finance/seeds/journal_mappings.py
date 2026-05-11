# verticals/finance/seeds/journal_mappings.py

JOURNAL_MAPPINGS = [
    {
        "transaction_type": "sales_invoice",
        "account_code": "1200",
        "entry_type": "debit",
        "amount_source": "total_amount",
        "order": 1,
    },
    {
        "transaction_type": "sales_invoice",
        "account_code": "4100",
        "entry_type": "credit",
        "amount_source": "subtotal",
        "order": 2,
    },
    {
        "transaction_type": "sales_invoice",
        "account_code": "2100",
        "entry_type": "credit",
        "amount_source": "tax_amount",
        "order": 3,
    },
    # =====================================
    # PURCHASE INVOICE
    # =====================================
    {
        "transaction_type": "purchase_invoice",
        "account_code": "5100",
        "entry_type": "debit",
        "amount_source": "subtotal",
        "order": 1,
    },
    {
        "transaction_type": "purchase_invoice",
        "account_code": "1150",
        "entry_type": "debit",
        "amount_source": "tax_amount",
        "order": 2,
    },
    {
        "transaction_type": "purchase_invoice",
        "account_code": "2200",
        "entry_type": "credit",
        "amount_source": "total_amount",
        "order": 3,
    },
    # =====================================
    # PAYMENT IN
    # =====================================
    {
        "transaction_type": "payment_in",
        "account_code": "1110",
        "entry_type": "debit",
        "amount_source": "total_amount",
        "order": 1,
    },
    {
        "transaction_type": "payment_in",
        "account_code": "1200",
        "entry_type": "credit",
        "amount_source": "total_amount",
        "order": 2,
    },
    # =====================================
    # PAYMENT OUT
    # =====================================
    {
        "transaction_type": "payment_out",
        "account_code": "2200",
        "entry_type": "debit",
        "amount_source": "total_amount",
        "order": 1,
    },
    {
        "transaction_type": "payment_out",
        "account_code": "1110",
        "entry_type": "credit",
        "amount_source": "total_amount",
        "order": 2,
    },
]
