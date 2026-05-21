# hrms/workflows/payroll/payroll_posting_workflow.py

from hrms.enums import PayrollStatus


def can_post_payroll(
    *,
    payroll,
):
    """
    Validate payroll posting workflow.
    """

    return payroll.status == PayrollStatus.PROCESSED
