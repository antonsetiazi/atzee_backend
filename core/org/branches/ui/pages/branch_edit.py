# core/org/branches/ui/pages/branch_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from core.org.branches.ui.pages._base_branch_form import (
    build_branch_form_page,
)

UI_PAGES = build_branch_form_page(
    key="branches.edit",
    domain="core",
    path="/settings/org/branches/:id/edit",
    submit_to="/branches/{id}/",
    method="PATCH",
    permissions=["core.branches.update"],
    title="Edit Branch",
    redirect_page="/settings/org/branches",
    extra_fields=[
        Field(key="id", label="Branch ID", type="hidden"),
    ],
)

register_ui_module_pages("core", UI_PAGES)