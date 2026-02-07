# accounting/fiscal_period/ui/pages/fiscal_period_create.py

from accounting.fiscal_period.ui.pages._base_fiscal_period_form import (
    build_fiscal_period_form_page,
)

UI_PAGES = build_fiscal_period_form_page(
    key="fiscal_period.create",
    domain="accounting",
    path="/accounting/fiscal-periods/create",
    submit_to="/accounting/fiscal-periods/",
    method="POST",
    permissions=["accounting.fiscal_period.add"],
    title="Create Fiscal Period",
    redirect_page="/accounting/fiscal-periods",
)
