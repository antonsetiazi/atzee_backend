from datetime import date, datetime
from django.db import transaction
from django.core.exceptions import ValidationError

from hr.payroll.models import PayrollRun, PayrollItem
from hr.payroll.calculators.base import BasePayrollCalculator
from hr.payroll.events import PayrollPostingEvent
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_payroll_run(
    *,
    tenant: Tenant,
    created_by: User,
    period_id: int,
    run_date: date,
    notes: str = ""
) -> PayrollRun:

    if PayrollRun.objects.filter(
        tenant=tenant,
        period_id=period_id
    ).exists():
        raise ValidationError(
            "Payroll already exists for this period."
        )

    return PayrollRun.objects.create(
        tenant=tenant,
        period_id=period_id,
        run_date=run_date,
        notes=notes,
        created_by=created_by
    )


@transaction.atomic
def generate_payroll_items(
    *,
    tenant: Tenant,
    payroll_run: PayrollRun,
    employee_ids: list[int],
    calculator: BasePayrollCalculator
) -> None:

    if payroll_run.status != PayrollRun.STATUS_DRAFT:
        raise ValidationError("Payroll already finalized.")

    PayrollItem.objects.filter(
        tenant=tenant,
        payroll_run=payroll_run
    ).delete()

    for employee_id in employee_ids:
        result = calculator.calculate(
            tenant=tenant,
            employee_id=employee_id,
            period_id=payroll_run.period_id
        )

        PayrollItem.objects.create(
            tenant=tenant,
            payroll_run=payroll_run,
            employee_id=employee_id,
            basic_salary=result.basic_salary,
            allowance=result.allowance,
            deduction=result.deduction,
            tax=result.tax,
            net_salary=result.net_salary
        )


@transaction.atomic
def finalize_payroll(
    *,
    tenant: Tenant,
    payroll_run_id: int,
    finalized_by: User
) -> PayrollRun:

    payroll = PayrollRun.objects.get(
        tenant=tenant,
        id=payroll_run_id
    )

    if payroll.status != PayrollRun.STATUS_DRAFT:
        raise ValidationError("Payroll already finalized.")

    payroll.status = PayrollRun.STATUS_FINALIZED
    payroll.updated_by = finalized_by
    payroll.save(update_fields=[
        "status",
        "updated_by",
        "updated_at",
    ])

    return payroll


def emit_payroll_events(
    *,
    payroll_run: PayrollRun
) -> list[PayrollPostingEvent]:

    if payroll_run.status != PayrollRun.STATUS_FINALIZED:
        raise ValidationError(
            "Payroll must be finalized first."
        )

    events = []

    for item in payroll_run.items.all():
        events.append(
            PayrollPostingEvent(
                tenant_id=payroll_run.tenant.id,
                payroll_run_id=payroll_run.id,
                employee_id=item.employee_id,
                period_id=payroll_run.period_id,
                gross_salary=item.basic_salary + item.allowance,
                tax=item.tax,
                net_salary=item.net_salary,
                expense_account_code="50100",
                payable_account_code="20100",
                occurred_at=datetime.utcnow()
            )
        )

    return events
