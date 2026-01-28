from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal
from datetime import datetime


@dataclass(frozen=True)
class PayrollPostingEvent:
    tenant_id: UUID
    payroll_run_id: int
    employee_id: int
    period_id: int

    gross_salary: Decimal
    tax: Decimal
    net_salary: Decimal

    expense_account_code: str
    payable_account_code: str

    occurred_at: datetime