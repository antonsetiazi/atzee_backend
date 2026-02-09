# core/classifications/labels/ui/pages/label_list.py

from core.classifications.labels.ui.pages._base_label_list import build_label_list_page

UI_PAGES = build_label_list_page(
    key="labels.list",
    domain="core",
    path="/settings/classifications/labels",
    data_source="/entities/core/labels.list/query/",
    permissions=["core.labels.view"],
    create_path="/settings/classifications/labels/create",
    edit_path="/settings/classifications/labels/{id}/edit",
    delete_endpoint="/labels/{id}/",
    search_mode="client",
)
