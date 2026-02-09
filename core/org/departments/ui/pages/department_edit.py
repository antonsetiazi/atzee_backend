# core/org/departments/ui/pages/department_edit.py

from core.ui.schema.field import Field
from core.org.departments.ui.pages._base_department_form import (
    build_department_form_page,
)

UI_PAGES = build_department_form_page(
    key="departments.edit",
    domain="core",
    path="/settings/org/departments/:id/edit",
    submit_to="/departments/{id}/",
    method="PATCH",
    permissions=["core.departments.update"],
    title="Edit Department",
    redirect_page="/settings/org/departments",
    extra_fields=[
        Field(key="id", label="Department ID", type="hidden"),
    ],
)
