# core/schedule/events/ui/pages/event_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from ._base_event_form import build_event_form_page

UI_PAGES = build_event_form_page(
    key="events.edit",
    domain="core",
    path="/core/events/:id/edit",
    submit_to="/schedule/events/{id}/",
    method="PATCH",
    permissions=["core.schedule.events.update"],
    title="Edit Event",
    redirect_page="/core/events",
    extra_fields=[
        Field(key="id", label="Event ID", type="hidden"),
    ],
)

register_ui_module_pages("core", UI_PAGES)