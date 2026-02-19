# core/org/departments/ui/pages/department_create.py

from core.ui.registry import register_ui_module_pages
from core.org.departments.ui.pages._base_department_form import (
    build_department_form_page,
)

UI_PAGES = build_department_form_page(
    key="departments.create",
    domain="core",
    path="/settings/org/departments/create",
    submit_to="/departments/",
    method="POST",
    permissions=["core.departments.add"],
    title="Create Department",
    redirect_page="/settings/org/departments",
)

register_ui_module_pages("core", UI_PAGES)