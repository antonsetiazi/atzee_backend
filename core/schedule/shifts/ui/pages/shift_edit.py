# core/schedule/shifts/ui/pages/shift_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from ._base_shift_form import build_shift_form_page

UI_PAGES = build_shift_form_page(
    key="shifts.edit",
    domain="core",
    path="/core/shifts/:id/edit",
    submit_to="/schedule/shifts/{id}/",
    method="PATCH",
    permissions=["core.schedule.shifts.update"],
    title="Edit Shift",
    redirect_page="/core/shifts",
    extra_fields=[
        Field(key="id", label="Shift ID", type="hidden"),
    ],
)

register_ui_module_pages("core", UI_PAGES)