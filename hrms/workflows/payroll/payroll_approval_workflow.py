# hrms/workflows/payroll/payroll_approval_workflow.py

from hrms.enums import PayrollStatus


def can_approve_payroll(
    *,
    payroll,
):
    """
    Validate payroll approval workflow.
    """

    return payroll.status == PayrollStatus.DRAFT
