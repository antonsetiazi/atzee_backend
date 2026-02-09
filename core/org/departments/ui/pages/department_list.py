# core/org/departments/ui/pages/department_list.py

from core.org.departments.ui.pages._base_department_list import (
    build_department_list_page,
)

UI_PAGES = build_department_list_page(
    key="departments.list",
    domain="core",
    path="/settings/org/departments",
    data_source="/entities/core/departments.list/query/",
    permissions=["core.departments.view"],
    create_path="/settings/org/departments/create",
    edit_path="/settings/org/departments/{id}/edit",
    delete_endpoint="/departments/{id}/",
    search_mode="client",
)
