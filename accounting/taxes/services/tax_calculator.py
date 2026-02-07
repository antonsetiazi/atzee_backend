# accounting/taxes/services/tax_calculator.py

from decimal import Decimal, ROUND_HALF_UP
from accounting.taxes.models import Tax


class TaxCalculator:
    @staticmethod
    def calculate(
        *,
        tax: Tax,
        base_amount: Decimal,
        rate: Decimal,
    ) -> Decimal:
        """
        Returns tax amount based on tax type.
        """

        if tax.type == "percentage":
            amount = (base_amount * rate) / Decimal("100")

        elif tax.type == "fixed":
            amount = rate

        elif tax.type == "withholding":
            amount = (base_amount * rate) / Decimal("100")

        else:
            raise ValueError(f"Unsupported tax type: {tax.type}")

        return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
