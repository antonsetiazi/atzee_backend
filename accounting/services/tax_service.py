# accounting/services/tax_service.py

from decimal import Decimal


class TaxService:

    @staticmethod
    def calculate_tax(
        *,
        subtotal,
        tax_rate
    ):

        subtotal = Decimal(subtotal)

        tax_rate = Decimal(tax_rate)

        tax_amount = (
            subtotal *
            tax_rate
        ) / Decimal("100")

        total = subtotal + tax_amount

        return {
            "subtotal": subtotal,
            "tax_amount": tax_amount,
            "total": total,
        }