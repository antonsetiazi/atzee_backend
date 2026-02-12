# core/schedule/events/ui/pages/event_create.py

from ._base_event_form import build_event_form_page

UI_PAGES = build_event_form_page(
    key="events.create",
    domain="core",
    path="/core/events/create",
    submit_to="/schedule/events/",
    method="POST",
    permissions=["core.schedule.events.add"],
    title="Create Event",
    redirect_page="/core/events",
)
