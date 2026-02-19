# core/schedule/holidays/ui/pages/holiday_create.py

from core.ui.registry import register_ui_module_pages
from ._base_holiday_form import build_holiday_form_page

UI_PAGES = build_holiday_form_page(
    key="holidays.create",
    domain="core",
    path="/core/holidays/create",
    submit_to="/schedule/holidays/",
    method="POST",
    permissions=["core.schedule.holidays.add"],
    title="Create Holiday",
    redirect_page="/core/holidays",
)

register_ui_module_pages("core", UI_PAGES)