from decimal import Decimal, ROUND_HALF_UP

def calculate_tax(amount: Decimal, rate: Decimal) -> Decimal:
    """
    amount: base amount
    rate: percentage (e.g. 11.00)
    """
    tax = amount * (rate / Decimal("100"))
    return tax.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )