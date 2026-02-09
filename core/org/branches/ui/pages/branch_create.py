# core/org/branches/ui/pages/branch_create.py

from core.org.branches.ui.pages._base_branch_form import (
    build_branch_form_page,
)

UI_PAGES = build_branch_form_page(
    key="branches.create",
    domain="core",
    path="/settings/org/branches/create",
    submit_to="/branches/",
    method="POST",
    permissions=["core.branches.add"],
    title="Create Branch",
    redirect_page="/settings/org/branches",
)
