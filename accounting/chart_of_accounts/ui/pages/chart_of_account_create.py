# accounting/chart_of_accounts/ui/pages/chart_of_account_create.py

from core.ui.registry import register_ui_module_pages
from accounting.chart_of_accounts.ui.pages._base_chart_of_account_form import (
    build_chart_of_account_form_page,
)

UI_PAGES = build_chart_of_account_form_page(
    key="chart_of_accounts.create",
    domain="accounting",
    path="/accounting/chart-of-accounts/create",
    submit_to="/accounting/chart-of-accounts/",
    method="POST",
    permissions=["accounting.chart_of_accounts.add"],
    title="Create Account",
    redirect_page="/accounting/chart-of-accounts",
)

register_ui_module_pages("accounting", UI_PAGES)