# core/schedule/recurrings/ui/pages/recurring_create.py

from core.ui.registry import register_ui_module_pages
from ._base_recurring_form import build_recurring_form_page

UI_PAGES = build_recurring_form_page(
    key="recurrings.create",
    domain="core",
    path="/core/recurrings/create",
    submit_to="/schedule/recurrings/",
    method="POST",
    permissions=["core.schedule.recurrings.add"],
    title="Create Recurring",
    redirect_page="/core/recurrings",
)

register_ui_module_pages("core", UI_PAGES)