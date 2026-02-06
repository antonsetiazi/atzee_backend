# hr/employees/ui/pages/employee_edit.py

from core.ui.schema.field import Field
from hr.employees.ui.pages._base_employee_form import (
    build_employee_form_page,
)

UI_PAGES = build_employee_form_page(
    key="employees.edit",
    domain="hr",
    path="/hr/employees/:id/edit",
    submit_to="/hr/employees/{id}/",
    method="PATCH",
    permissions=["hr.employees.update"],
    title="Edit Employee",
    redirect_page="/hr/employees",
    extra_fields=[
        Field(
            key="id",
            label="Employee ID",
            type="hidden",
        ),
    ],
)
