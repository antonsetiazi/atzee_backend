# core/fees/services/fee_engine.py

from decimal import Decimal
from typing import List

from core.fees.types import FeeInput, FeeResult, FeeItemResult
from core.fees.services.selectors import get_active_fees
from core.fees.services.calculators import (
    calculate_percent_fee,
    calculate_fixed_fee,
)


class FeeEngine:
    def calculate(self, data: FeeInput) -> FeeResult:
        fees = get_active_fees(data.tenant_id)

        customer_fees: List[FeeItemResult] = []
        partner_fees: List[FeeItemResult] = []

        total_customer_fee = Decimal("0")
        total_partner_fee = Decimal("0")

        for fee in fees:
            # ======================
            # CALCULATE
            # ======================
            if fee.fee_type == "percent":
                fee_amount = calculate_percent_fee(
                    data.amount,
                    fee.value
                )
            else:
                fee_amount = calculate_fixed_fee(
                    fee.value
                )

            item = FeeItemResult(
                name=fee.name,
                fee_type=fee.fee_type,
                applies_to=fee.applies_to,
                value=fee.value,
                amount=fee_amount,
            )

            # ======================
            # SPLIT
            # ======================
            if fee.applies_to == "customer":
                customer_fees.append(item)
                total_customer_fee += fee_amount
            else:
                partner_fees.append(item)
                total_partner_fee += fee_amount

        # ======================
        # FINAL CALCULATION
        # ======================
        final_customer_pay = data.amount + total_customer_fee
        final_partner_receive = data.amount - total_partner_fee

        return FeeResult(
            base_amount=data.amount,

            customer_fees=customer_fees,
            partner_fees=partner_fees,

            total_customer_fee=total_customer_fee,
            total_partner_fee=total_partner_fee,

            final_customer_pay=final_customer_pay,
            final_partner_receive=final_partner_receive,
        )