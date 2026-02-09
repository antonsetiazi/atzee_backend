# core/classifications/tags/ui/pages/tag_list.py

from core.classifications.tags.ui.pages._base_tag_list import build_tag_list_page

UI_PAGES = build_tag_list_page(
    key="tags.list",
    domain="core",
    path="/settings/classifications/tags",
    data_source="/entities/core/tags.list/query/",
    permissions=["core.tags.view"],
    create_path="/settings/classifications/tags/create",
    edit_path="/settings/classifications/tags/{id}/edit",
    delete_endpoint="/tags/{id}/",
    search_mode="client",
)
