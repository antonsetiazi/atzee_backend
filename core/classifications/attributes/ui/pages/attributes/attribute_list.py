# core/classifications/attributes/ui/pages/attributes/attribute_list.py

from ._base_attribute_list import (
    build_attribute_list_page,
)

UI_PAGES = build_attribute_list_page(
    key="attributes.list",
    domain="core",
    path="/settings/classifications/attributes",
    data_source="/entities/core/attributes.list/query/",
    permissions=["core.attributes.view"],
    create_path="/settings/classifications/attributes/create",
    edit_path="/settings/classifications/attributes/{id}/edit",
    delete_endpoint="/attributes/{id}/",
    search_mode="client",
)
