# core/master/currencies/ui/pages/currency_list.py

from core.ui.registry import register_ui_module_pages
from core.master.currencies.ui.pages._base_currency_list import (
    build_currency_list_page,
)

UI_PAGES = build_currency_list_page(
    key="currencies.list",
    domain="core",
    path="/settings/master/currencies",
    data_source="/entities/core/currencies.list/query/",
    permissions=["core.currencies.view"],
    create_path="/settings/master/currencies/create",
    edit_path="/settings/master/currencies/{id}/edit",
    search_mode="client",
)

register_ui_module_pages("core", UI_PAGES)