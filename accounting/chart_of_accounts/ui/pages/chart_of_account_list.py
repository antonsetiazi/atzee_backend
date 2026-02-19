# src/accounting/chart_of_accounts/ui/pages/chart_of_account_list.py

from core.ui.registry import register_ui_module_pages
from accounting.chart_of_accounts.ui.pages._base_chart_of_account_list import (
    build_chart_of_account_list_page,
)

UI_PAGES = build_chart_of_account_list_page(
    key="chart_of_accounts.list",
    domain="accounting",
    path="/accounting/chart-of-accounts",
    data_source="/entities/accounting/chart_of_accounts.list/query/",
    permissions=["accounting.chart_of_accounts.view"],
    create_path="/accounting/chart-of-accounts/create",
    edit_path="/accounting/chart-of-accounts/{id}/edit",
    delete_endpoint="/accounting/chart-of-accounts/{id}/",
    search_mode="client"
)

register_ui_module_pages("accounting", UI_PAGES)