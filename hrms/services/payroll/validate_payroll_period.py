# hrms/services/payroll/validate_payroll_period.py

from hrms.models import Payroll


def validate_payroll_period(
    *,
    tenant,
    employee,
    payroll_period,
):
    """
    Prevent duplicate payroll generation.
    """

    exists = Payroll.objects.filter(
        tenant=tenant,
        employee=employee,
        payroll_period=payroll_period,
        is_deleted=False,
    ).exists()

    return not exists
