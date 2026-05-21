# hrms/services/payroll/calculate_net_salary.py


def calculate_net_salary(
    *,
    basic_salary,
    allowance_amount,
    overtime_amount,
    deduction_amount,
):
    """
    Calculate employee net salary.
    """

    return basic_salary + allowance_amount + overtime_amount - deduction_amount
