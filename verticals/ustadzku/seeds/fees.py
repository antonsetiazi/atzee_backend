# verticals/ustadzku/seeds/fees.py

FEES = [
    {
        "name": "Default Commission",
        "fee_type": "percent",
        "value": 10,
        "applies_to": "partner",
    },
    {
        "name": "Service Fee",
        "fee_type": "fixed",
        "value": 3000,
        "applies_to": "customer",
    },
]