# hr/employees/ui/pages/employee_list.py

from hr.employees.ui.pages._base_employee_list import (
    build_employee_list_page,
)

UI_PAGES = build_employee_list_page(
    key="employees.list",
    domain="hr",
    path="/hr/employees",
    data_source="/entities/hr/employees.list/query/",
    permissions=["hr.employees.view"],
    create_path="/hr/employees/create",
    edit_path="/hr/employees/{id}/edit",
    delete_endpoint="/hr/employees/{id}/",
    search_mode="client"
)