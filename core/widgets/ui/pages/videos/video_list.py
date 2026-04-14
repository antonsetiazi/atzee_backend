# core/widgets/ui/pages/videos/video_list.py

from core.ui.registry import register_ui_module_pages
from core.widgets.ui.pages._base_widget_list import (
    build_widget_list_page,
)

UI_PAGES = build_widget_list_page(
    key="widgets.list",
    domain="core",
    title_page="UI Widgets",
    subtitle_page="Manage dynamic UI widgets and frontend components",
    path="/admin/widgets",
    data_source="/entities/core/widgets.list/query/",
    permissions=["core.widgets.view"],
    create_path="/admin/widgets/create",
    edit_path="/admin/widgets/{id}/edit",
    delete_endpoint="/core/widgets/{id}/",
    search_mode="client",
)

register_ui_module_pages("core", UI_PAGES)