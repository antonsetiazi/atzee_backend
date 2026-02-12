# core/schedule/holidays/ui/pages/holiday_list.py

from ._base_holiday_list import build_holiday_list_page

UI_PAGES = build_holiday_list_page(
    key="holidays.list",
    domain="core",
    path="/core/holidays",
    data_source="/entities/core/schedule.holidays.list/query/",
    permissions=["core.schedule.holidays.view"],
    create_path="/core/holidays/create",
    edit_path="/core/holidays/{id}/edit",
    delete_endpoint="/schedule/holidays/{id}/",
    search_mode="client",
)
