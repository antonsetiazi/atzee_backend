# core/schedule/recurrings/ui/pages/recurring_edit.py

from core.ui.schema.field import Field
from ._base_recurring_form import build_recurring_form_page

UI_PAGES = build_recurring_form_page(
    key="recurrings.edit",
    domain="core",
    path="/core/recurrings/:id/edit",
    submit_to="/schedule/recurrings/{id}/",
    method="PATCH",
    permissions=["core.schedule.recurrings.update"],
    title="Edit Recurring",
    redirect_page="/core/recurrings",
    extra_fields=[
        Field(key="id", label="Recurring ID", type="hidden"),
    ],
)
