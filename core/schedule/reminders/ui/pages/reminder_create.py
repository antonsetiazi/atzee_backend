# core/schedule/reminders/ui/pages/reminder_create.py

from ._base_reminder_form import build_reminder_form_page

UI_PAGES = build_reminder_form_page(
    key="reminders.create",
    domain="core",
    path="/core/reminders/create",
    submit_to="/schedule/reminders/",
    method="POST",
    permissions=["core.schedule.reminders.add"],
    title="Create Reminder",
    redirect_page="/core/reminders",
)
