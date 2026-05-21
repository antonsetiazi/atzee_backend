# hrms/services/payroll/post_payroll.py

from django.db import transaction
from django.utils import timezone

from hrms.enums import PayrollStatus


@transaction.atomic
def post_payroll(
    *,
    payroll,
    updated_by=None,
):
    """
    Post payroll into financial system.
    """

    payroll.status = PayrollStatus.PAID
    payroll.processed_at = timezone.now()
    payroll.updated_by = updated_by
    payroll.save()

    # future:
    # accounting journal posting
    # cash disbursement
    # liability settlement
    # payslip distribution
    # activity log

    return payroll
