# core/schedule/shifts/ui/pages/shift_create.py

from core.ui.registry import register_ui_module_pages
from ._base_shift_form import build_shift_form_page

UI_PAGES = build_shift_form_page(
    key="shifts.create",
    domain="core",
    path="/core/shifts/create",
    submit_to="/schedule/shifts/",
    method="POST",
    permissions=["core.schedule.shifts.add"],
    title="Create Shift",
    redirect_page="/core/shifts",
)

register_ui_module_pages("core", UI_PAGES)