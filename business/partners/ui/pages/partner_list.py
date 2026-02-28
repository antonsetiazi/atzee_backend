# business/partners/ui/pages/partner_list.py

from core.ui.registry import register_ui_module_pages
from business.partners.ui.pages._base_partner_list import (
    build_partner_list_page,
)

from business.enum.permissions import BusinessPermission


UI_PAGES = build_partner_list_page(
    key="partners.list",
    domain="business",
    path="/business/partners",
    data_source="/entities/business/partners.list/query/",
    permissions=[BusinessPermission.PARTNERS_VIEW],
    create_path="/business/partners/create",
    edit_path="/business/partners/{id}/edit",
    delete_endpoint="/business/partners/{id}/",
    search_mode="client"
)

register_ui_module_pages("business", UI_PAGES) 