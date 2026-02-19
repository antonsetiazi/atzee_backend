# core/geo/timezones/ui/pages/timezone_list.py

from core.ui.registry import register_ui_module_pages
from core.geo.timezones.ui.pages._base_timezone_list import (
    build_timezone_list_page,
)

UI_PAGES = build_timezone_list_page(
    key="timezones.list",
    domain="core",
    path="/settings/geo/timezones",
    data_source="/entities/core/timezones.list/query/",
    permissions=["core.timezones.view"],
    create_path="/settings/geo/timezones/create",
    edit_path="/settings/geo/timezones/{id}/edit",
    delete_endpoint="/timezones/{id}/",
)

register_ui_module_pages("core", UI_PAGES)