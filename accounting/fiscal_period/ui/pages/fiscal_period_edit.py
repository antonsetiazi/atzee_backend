# accounting/fiscal_period/ui/pages/fiscal_period_edit.py

from core.ui.schema.field import Field
from accounting.fiscal_period.ui.pages._base_fiscal_period_form import (
    build_fiscal_period_form_page,
)

UI_PAGES = build_fiscal_period_form_page(
    key="fiscal_period.edit",
    domain="accounting",
    path="/accounting/fiscal-periods/:id/edit",
    submit_to="/accounting/fiscal-periods/{id}/",
    method="PATCH",
    permissions=["accounting.fiscal_period.update"],
    title="Edit Fiscal Period",
    redirect_page="/accounting/fiscal-periods",
    extra_fields=[
        Field(
            key="id",
            label="Fiscal Period ID",
            type="hidden",
        ),
    ],
)
