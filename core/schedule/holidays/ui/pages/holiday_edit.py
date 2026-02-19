# core/schedule/holidays/ui/pages/holiday_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from ._base_holiday_form import build_holiday_form_page

UI_PAGES = build_holiday_form_page(
    key="holidays.edit",
    domain="core",
    path="/core/holidays/:id/edit",
    submit_to="/schedule/holidays/{id}/",
    method="PATCH",
    permissions=["core.schedule.holidays.update"],
    title="Edit Holiday",
    redirect_page="/core/holidays",
    extra_fields=[
        Field(key="id", label="Holiday ID", type="hidden"),
    ],
)

register_ui_module_pages("core", UI_PAGES)