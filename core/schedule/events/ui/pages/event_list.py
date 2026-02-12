# core/schedule/events/ui/pages/event_list.py

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
