# core/widgets/ui/pages/banners/banner_list.py

from core.ui.registry import register_ui_module_pages
from core.widgets.ui.pages._base_widget_list import (
    build_widget_list_page,
)

UI_PAGES = build_widget_list_page(
    key="widgets.banners.list",
    domain="core",
    path="/widgets/banners",
    title_page="Banner",
    data_source="/entities/core/widgets.list/query/",
    permissions=["core.widgets.view"],
    create_label="Create Banner",
    create_path="/widgets/banners/create",
    edit_path="/widgets/banners/{id}/edit",
    delete_endpoint="/widgets/{id}/",
    default_query={
        "type": "banner"
    }
)

register_ui_module_pages("core", UI_PAGES)