# core/schedule/events/ui/pages/event_list.py

from core.ui.registry import register_ui_module_pages
from ._base_event_list import build_event_list_page

UI_PAGES = build_event_list_page(
    key="events.list",
    domain="core",
    path="/core/events",
    data_source="/entities/core/schedule.events.list/query/",
    permissions=["core.schedule.events.view"],
    create_path="/core/events/create",
    edit_path="/core/events/{id}/edit",
    delete_endpoint="/schedule/events/{id}/",
    search_mode="client",
)

register_ui_module_pages("core", UI_PAGES)
