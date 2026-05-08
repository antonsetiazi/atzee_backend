# verticals/finance/seeds/accounts.py

ACCOUNTS = [
    {
        "code": "1000",
        "name": "Assets",
        "account_type": "asset",
        "normal_balance": "debit",
        "is_group": True,
        "children": [
            {
                "code": "1100",
                "name": "Cash",
                "account_type": "asset",
                "normal_balance": "debit",
                "is_group": False,
            },
            {
                "code": "1110",
                "name": "Bank BCA",
                "account_type": "asset",
                "normal_balance": "debit",
                "is_group": False,
            },
            {
                "code": "1120",
                "name": "Bank Mandiri",
                "account_type": "asset",
                "normal_balance": "debit",
                "is_group": False,
            },
            {
                "code": "1130",
                "name": "Bank BNI",
                "account_type": "asset",
                "normal_balance": "debit",
                "is_group": False,
            },
            {
                "code": "1200",
                "name": "Accounts Receivable",
                "account_type": "asset",
                "normal_balance": "debit",
                "is_group": False,
            },
        ],
    },
    {
        "code": "2000",
        "name": "Liabilities",
        "account_type": "liability",
        "normal_balance": "credit",
        "is_group": True,
        "children": [
            {
                "code": "2100",
                "name": "Tax Payable",
                "account_type": "liability",
                "normal_balance": "credit",
                "is_group": False,
            },
            {
                "code": "2200",
                "name": "Accounts Payable",
                "account_type": "liability",
                "normal_balance": "credit",
                "is_group": False,
            },
        ],
    },
    {
        "code": "3000",
        "name": "Equity",
        "account_type": "equity",
        "normal_balance": "credit",
        "is_group": True,
    },
    {
        "code": "4000",
        "name": "Revenue",
        "account_type": "revenue",
        "normal_balance": "credit",
        "is_group": True,
        "children": [
            {
                "code": "4100",
                "name": "Sales Revenue",
                "account_type": "revenue",
                "normal_balance": "credit",
                "is_group": False,
            }
        ],
    },
    {
        "code": "5000",
        "name": "Expenses",
        "account_type": "expense",
        "normal_balance": "debit",
        "is_group": True,
        "children": [
            {
                "code": "5100",
                "name": "Electricity Expense",
                "account_type": "expense",
                "normal_balance": "debit",
                "is_group": False,
            },
            {
                "code": "5200",
                "name": "Internet Expense",
                "account_type": "expense",
                "normal_balance": "debit",
                "is_group": False,
            },
        ],
    },
]
