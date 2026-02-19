# hr/employees/ui/pages/employee_create.py

from core.ui.registry import register_ui_module_pages
from hr.employees.ui.pages._base_employee_form import (
    build_employee_form_page,
)

UI_PAGES = build_employee_form_page(
    key="employees.create",
    domain="hr",
    path="/hr/employees/create",
    submit_to="/hr/employees/",
    method="POST",
    permissions=["hr.employees.add"],
    title="Create Employee",
    redirect_page="/hr/employees",
)

register_ui_module_pages("hr", UI_PAGES)