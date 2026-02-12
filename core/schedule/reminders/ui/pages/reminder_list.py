# core/schedule/reminders/ui/pages/reminder_list.py

from ._base_reminder_list import build_reminder_list_page

UI_PAGES = build_reminder_list_page(
    key="reminders.list",
    domain="core",
    path="/core/reminders",
    data_source="/entities/core/schedule.reminders.list/query/",
    permissions=["core.schedule.reminders.view"],
    create_path="/core/reminders/create",
    edit_path="/core/reminders/{id}/edit",
    delete_endpoint="/schedule/reminders/{id}/",
    search_mode="client",
)
