# core/schedule/shifts/ui/pages/shift_create.py

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
