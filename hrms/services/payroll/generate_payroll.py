# hrms/services/payroll/generate_payroll.py

from django.db import transaction

from hrms.enums import PayrollStatus
from hrms.models import Payroll
from hrms.services.payroll.calculate_allowance import (
    calculate_allowance,
)
from hrms.services.payroll.calculate_basic_salary import (
    calculate_basic_salary,
)
from hrms.services.payroll.calculate_deduction import (
    calculate_deduction,
)
from hrms.services.payroll.calculate_net_salary import (
    calculate_net_salary,
)
from hrms.services.payroll.calculate_overtime_pay import (
    calculate_overtime_pay,
)
from hrms.services.payroll.validate_payroll_period import (
    validate_payroll_period,
)


@transaction.atomic
def generate_payroll(
    *,
    tenant,
    employee,
    payroll_period,
    created_by=None,
):
    """
    Generate employee payroll.
    """

    is_valid = validate_payroll_period(
        tenant=tenant,
        employee=employee,
        payroll_period=payroll_period,
    )

    if not is_valid:
        raise ValueError("Payroll already exists for this period.")

    basic_salary = calculate_basic_salary(
        employee=employee,
    )

    allowance_amount = calculate_allowance(
        employee=employee,
        payroll_period=payroll_period,
    )

    overtime_amount = calculate_overtime_pay(
        employee=employee,
        payroll_period=payroll_period,
    )

    deduction_amount = calculate_deduction(
        employee=employee,
        payroll_period=payroll_period,
    )

    net_salary = calculate_net_salary(
        basic_salary=basic_salary,
        allowance_amount=allowance_amount,
        overtime_amount=overtime_amount,
        deduction_amount=deduction_amount,
    )

    payroll = Payroll.objects.create(
        tenant=tenant,
        employee=employee,
        payroll_period=payroll_period,
        basic_salary=basic_salary,
        allowance_amount=(allowance_amount + overtime_amount),
        deduction_amount=deduction_amount,
        net_salary=net_salary,
        status=PayrollStatus.DRAFT,
        created_by=created_by,
        updated_by=created_by,
    )

    # future:
    # payslip generation
    # payroll workflow
    # accounting integration
    # activity log

    return payroll
