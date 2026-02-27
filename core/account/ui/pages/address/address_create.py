# core/account/ui/pages/address/address_create.py

from core.ui.registry import register_ui_module_pages
from core.account.ui.pages.address._base_address_form import (
    build_address_form_page,
)

UI_PAGES = build_address_form_page(
    key="account.address.create",
    domain="core",
    path="/account/address/create",
    submit_to="/account/address/",
    method="POST",
    permissions=["core.account.address.create"],
    title="Add New Address",
    redirect_page="/account/address",
)

register_ui_module_pages("core", UI_PAGES)