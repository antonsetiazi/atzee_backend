# core/account/ui/pages/address/address_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from core.account.ui.pages.address._base_address_form import (
    build_address_form_page,
)

UI_PAGES = build_address_form_page(
    key="account.address.edit",
    domain="core",
    mode="edit",
    path="/admin/account/address/:id/edit",
    submit_to="/account/address/{id}/",
    method="PATCH",
    permissions=["core.account.address.update"],
    title="Edit Address",
    redirect_page="/account/address",
    extra_fields=[
        Field(
            key="id",
            label="Address ID",
            type="hidden",
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)