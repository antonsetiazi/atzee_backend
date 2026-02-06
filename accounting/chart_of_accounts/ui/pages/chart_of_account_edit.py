# accounting/chart_of_accounts/ui/pages/chart_of_account_edit.py

from core.ui.schema.field import Field
from accounting.chart_of_accounts.ui.pages._base_chart_of_account_form import (
    build_chart_of_account_form_page,
)

UI_PAGES = build_chart_of_account_form_page(
    key="chart_of_accounts.edit",
    domain="accounting",
    path="/accounting/chart-of-accounts/:id/edit",
    submit_to="/accounting/chart-of-accounts/{id}/",
    method="PATCH",
    permissions=["accounting.chart-of-accounts.update"],
    title="Edit Account",
    redirect_page="/accounting/chart-of-accounts",
    extra_fields=[
        Field(
            key="id",
            label="Account ID",
            type="hidden",
        ),
    ],
)
