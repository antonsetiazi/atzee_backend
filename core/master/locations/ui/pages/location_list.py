# core/master/locations/ui/pages/location_list.py

from core.ui.registry import register_ui_module_pages
from core.master.locations.ui.pages._base_location_list import (
    build_location_list_page,
)

UI_PAGES = build_location_list_page(
    key="locations.list",
    domain="core",
    path="/settings/master/location",
    data_source="/entities/core/locations.list/query/",
    permissions=["core.location.view"],
    create_path="/settings/master/location/create",
    edit_path="/settings/master/location/{id}/edit",
    delete_endpoint="/locations/{id}/",
    search_mode="client",
)

register_ui_module_pages("core", UI_PAGES)