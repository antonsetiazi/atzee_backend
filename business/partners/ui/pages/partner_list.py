# business/partners/ui/pages/partner_list.py

from business.partners.ui.pages._base_partner_list import (
    build_partner_list_page,
)

UI_PAGES = build_partner_list_page(
    key="partners.list",
    domain="business",
    path="/business/partners",
    data_source="/entities/business/partners.list/query/",
    permissions=["business.partners.view"],
    create_path="/business/partners/create",
    edit_path="/business/partners/{id}/edit",
    delete_endpoint="/business/partners/{id}/",
    search_mode="client"
)