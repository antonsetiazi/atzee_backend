# core/geo/regions/ui/pages/region_list.py

from core.ui.registry import register_ui_module_pages
from core.geo.regions.ui.pages._base_region_list import (
    build_region_list_page,
)

UI_PAGES = build_region_list_page(
    key="regions.list",
    domain="core",
    path="/settings/geo/regions",
    data_source="/entities/core/regions.list/query/",
    permissions=["core.regions.view"],
    create_path="/settings/geo/regions/create",
    edit_path="/settings/geo/regions/{id}/edit",
    delete_endpoint="/regions/{id}/",
)

register_ui_module_pages("core", UI_PAGES)