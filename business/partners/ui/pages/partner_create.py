# business/partners/ui/pages/partner_create.py

from business.partners.ui.pages._base_partner_form import (
    build_partner_form_page,
)

UI_PAGES = build_partner_form_page(
    key="partners.create",
    domain="business",
    path="/business/partners/create",
    submit_to="/business/partners/",
    method="POST",
    permissions=["business.partners.add"],
    title="Create Partner",
    redirect_page="/business/partners",
)
