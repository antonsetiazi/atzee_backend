# verticals/finance/seeds/taxes.py

TAXES = [
    {
        "code": "PPN11",
        "name": "PPN 11%",
        "tax_type": "sales",
        "rate": 11,
    },

    {
        "code": "PPN12",
        "name": "PPN 12%",
        "tax_type": "sales",
        "rate": 12,
    },

    {
        "code": "PPH23",
        "name": "PPh 23",
        "tax_type": "withholding",
        "rate": 2,
    },

    {
        "code": "NON_TAX",
        "name": "Non Tax",
        "tax_type": "sales",
        "rate": 0,
    },
]