# hrms/selectors/payroll_selector.py

from django.db.models import Sum

from hrms.enums import PayrollStatus
from hrms.models import Payroll


def get_employee_payroll_history(
    tenant,
    employee_id,
):
    return Payroll.objects.filter(
        tenant=tenant,
        employee_id=employee_id,
        is_deleted=False,
    ).order_by("-created_at")


def get_processed_payrolls(
    tenant,
):
    return Payroll.objects.filter(
        tenant=tenant,
        status=PayrollStatus.PROCESSED,
        is_deleted=False,
    ).select_related(
        "employee",
    )


def get_payroll_total_by_period(
    tenant,
    payroll_period,
):
    return Payroll.objects.filter(
        tenant=tenant,
        payroll_period=payroll_period,
        is_deleted=False,
    ).aggregate(total_salary=Sum("net_salary"))
