# core/classifications/categories/ui/pages/category_list.py

from core.ui.registry import register_ui_module_pages
from core.classifications.categories.ui.pages._base_category_list import (
    build_category_list_page,
)

UI_PAGES = build_category_list_page(
    key="categories.list",
    domain="core",
    path="/settings/classifications/categories",
    data_source="/entities/core/categories.list/query/",
    permissions=["core.categories.view"],
    create_path="/settings/classifications/categories/create",
    edit_path="/settings/classifications/categories/{id}/edit",
    delete_endpoint="/categories/{id}/",
    search_mode="client",
)

register_ui_module_pages("core", UI_PAGES)