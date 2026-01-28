from decimal import Decimal
from abc import ABC, abstractmethod


class PayrollCalculationResult:
    def __init__(
        self,
        *,
        basic_salary: Decimal,
        allowance: Decimal,
        deduction: Decimal,
        tax: Decimal,
    ):
        self.basic_salary = basic_salary
        self.allowance = allowance
        self.deduction = deduction
        self.tax = tax

    
    @property
    def net_salary(self) -> Decimal:
        return (
            self.basic_salary
            + self.allowance
            - self.deduction
            - self.tax
        )
    

class BasePayrollCalculator(ABC):
    """
    Strategy interface.
    """

    @abstractmethod
    def calculate(
        self,
        *,
        tenant,
        employee_id: int,
        period_id: int
    ) -> PayrollCalculationResult:
        pass