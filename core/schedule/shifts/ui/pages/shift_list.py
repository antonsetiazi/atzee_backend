# core/schedule/shifts/ui/pages/shift_list.py

from core.ui.registry import register_ui_module_pages
from ._base_shift_list import build_shift_list_page

UI_PAGES = build_shift_list_page(
    key="shifts.list",
    domain="core",
    path="/core/shifts",
    data_source="/entities/core/schedule.shifts.list/query/",
    permissions=["core.schedule.shifts.view"],
    create_path="/core/shifts/create",
    edit_path="/core/shifts/{id}/edit",
    delete_endpoint="/schedule/shifts/{id}/",
    search_mode="client",
)

register_ui_module_pages("core", UI_PAGES)