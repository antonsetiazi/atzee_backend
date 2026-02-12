# core/schedule/reminders/ui/pages/reminder_edit.py

from core.ui.schema.field import Field
from ._base_reminder_form import build_reminder_form_page

UI_PAGES = build_reminder_form_page(
    key="reminders.edit",
    domain="core",
    path="/core/reminders/:id/edit",
    submit_to="/schedule/reminders/{id}/",
    method="PATCH",
    permissions=["core.schedule.reminders.update"],
    title="Edit Reminder",
    redirect_page="/core/reminders",
    extra_fields=[
        Field(key="id", label="Reminder ID", type="hidden"),
    ],
)
