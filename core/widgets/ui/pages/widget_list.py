# core/widgets/ui/pages/widget_list.py

from core.widgets.ui.pages._base_widget_list import (
    build_widget_list_page,
)

UI_PAGES = build_widget_list_page(
    key="widgets.list",
    domain="core",
    path="/settings/widgets",
    title_page="Widgets",
    data_source="/entities/core/widgets.list/query/",
    permissions=["core.widgets.view"],
    create_label="Create Widget",
    create_path="/settings/widgets/create",
    edit_path="/settings/widgets/{id}/edit",
    delete_endpoint="/widgets/{id}/",
)
