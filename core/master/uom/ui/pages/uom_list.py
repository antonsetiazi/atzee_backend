# core/master/uom/ui/pages/uom_list.py

from core.ui.registry import register_ui_module_pages
from core.master.uom.ui.pages._base_uom_list import (
    build_uom_list_page,
)

UI_PAGES = build_uom_list_page(
    key="uom.list",
    domain="core",
    path="/settings/master/uom",
    data_source="/entities/core/uom.list/query/",
    permissions=["core.uom.view"],
    create_path="/settings/master/uom/create",
    edit_path="/settings/master/uom/{id}/edit",
    delete_endpoint="/uoms/{id}/",
    search_mode="client"
)

register_ui_module_pages("core", UI_PAGES)