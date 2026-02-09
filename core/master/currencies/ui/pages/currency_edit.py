# core/master/currencies/ui/pages/currency_edit.py

from core.ui.schema.field import Field
from core.master.currencies.ui.pages._base_currency_form import (
    build_currency_form_page,
)

UI_PAGES = build_currency_form_page(
    key="currencies.edit",
    domain="core",
    path="/settings/master/currencies/:id/edit",
    submit_to="/currencies/{id}/",
    method="PATCH",
    permissions=["core.currencies.update"],
    title="Edit Currency",
    redirect_page="/settings/master/currencies",
    extra_fields=[
        Field(key="id", label="Currency ID", type="hidden"),
    ],
)
