# core/master/currencies/ui/pages/currency_create.py

from core.ui.registry import register_ui_module_pages
from core.master.currencies.ui.pages._base_currency_form import (
    build_currency_form_page,
)

UI_PAGES = build_currency_form_page(
    key="currencies.create",
    domain="core",
    path="/settings/master/currencies/create",
    submit_to="/currencies/",
    method="POST",
    permissions=["core.currencies.add"],
    title="Create Currency",
    redirect_page="/settings/master/currencies",
)

register_ui_module_pages("core", UI_PAGES)