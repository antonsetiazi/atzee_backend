# business/partners/ui/pages/partner_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from business.partners.ui.pages._base_partner_form import (
    build_partner_form_page,
)

UI_PAGES = build_partner_form_page(
    key="partners.edit",
    domain="business",
    path="/business/partners/:id/edit",
    submit_to="/business/partners/{id}/",
    method="PATCH",
    permissions=["business.partners.update"],
    title="Edit Partner",
    redirect_page="/business/partners",
    extra_fields=[
        Field(
            key="id",
            label="Partner ID",
            type="hidden",
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)