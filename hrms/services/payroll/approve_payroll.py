# hrms/services/payroll/approve_payroll.py

from django.db import transaction

from hrms.enums import PayrollStatus


@transaction.atomic
def approve_payroll(
    *,
    payroll,
    approved_by=None,
):
    """
    Approve payroll before posting.
    """

    payroll.status = PayrollStatus.PROCESSED
    payroll.updated_by = approved_by
    payroll.save()

    # future:
    # approval workflow
    # payroll locking
    # notifications

    return payroll
