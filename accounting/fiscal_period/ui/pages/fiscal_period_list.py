# accounting/fiscal_period/ui/pages/fiscal_period_list.py

from core.ui.registry import register_ui_module_pages
from accounting.fiscal_period.ui.pages._base_fiscal_period_list import (
    build_fiscal_period_list_page,
)

UI_PAGES = build_fiscal_period_list_page(
    key="fiscal_period.list",
    domain="accounting",
    path="/accounting/fiscal-periods",
    data_source="/entities/accounting/fiscal_period.list/query/",
    permissions=["accounting.fiscal_period.view"],
    create_path="/accounting/fiscal-periods/create",
    edit_path="/accounting/fiscal-periods/{id}/edit",
    close_endpoint="/api/fiscal-periods/{id}/close/",
    search_mode="client",
)

register_ui_module_pages("accounting", UI_PAGES)