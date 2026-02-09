# core/org/branches/ui/pages/branch_list.py

from core.org.branches.ui.pages._base_branch_list import (
    build_branch_list_page,
)

UI_PAGES = build_branch_list_page(
    key="branches.list",
    domain="core",
    path="/settings/org/branches",
    data_source="/entities/core/branches.list/query/",
    permissions=["core.branches.view"],
    create_path="/settings/org/branches/create",
    edit_path="/settings/org/branches/{id}/edit",
    delete_endpoint="/branches/{id}/",
    search_mode="client",
)
