# core/schedule/recurrings/ui/pages/recurring_list.py

from ._base_recurring_list import build_recurring_list_page

UI_PAGES = build_recurring_list_page(
    key="recurrings.list",
    domain="core",
    path="/core/recurrings",
    data_source="/entities/core/schedule.recurrings.list/query/",
    permissions=["core.schedule.recurrings.view"],
    create_path="/core/recurrings/create",
    edit_path="/core/recurrings/{id}/edit",
    delete_endpoint="/schedule/recurrings/{id}/",
    search_mode="client",
)
