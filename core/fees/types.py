# core/fees/types.py

from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional


@dataclass
class FeeInput:
    tenant_id: str
    amount: Decimal

    category: Optional[str] = None
    partner_id: Optional[str] = None


@dataclass
class FeeItemResult:
    name: str
    fee_type: str  # percent | fixed
    applies_to: str  # customer | partner

    value: Decimal
    amount: Decimal


@dataclass
class FeeResult:
    base_amount: Decimal

    customer_fees: List[FeeItemResult]
    partner_fees: List[FeeItemResult]

    total_customer_fee: Decimal
    total_partner_fee: Decimal

    final_customer_pay: Decimal
    final_partner_receive: Decimal