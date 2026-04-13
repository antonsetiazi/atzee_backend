# core/fees/services/calculators.py

from decimal import Decimal


def calculate_percent_fee(amount: Decimal, percent: Decimal) -> Decimal:
    return (amount * percent) / Decimal("100")


def calculate_fixed_fee(value: Decimal) -> Decimal:
    return value