# core/widgets/ui/pages/videos/video_list.py

from core.ui.registry import register_ui_module_pages
from core.widgets.ui.pages._base_widget_list import (
    build_widget_list_page,
)

UI_PAGES = build_widget_list_page(
    key="widgets.videos.list",
    domain="core",
    path="/widgets/videos",
    title_page="Videos",
    data_source="/entities/core/widgets.list/query/",
    permissions=["core.widgets.view"],
    create_label="Create Video",
    create_path="/widgets/videos/create",
    edit_path="/widgets/videos/{id}/edit",
    delete_endpoint="/widgets/{id}/",
    default_query={
        "type": "video"
    }
)

register_ui_module_pages("core", UI_PAGES)