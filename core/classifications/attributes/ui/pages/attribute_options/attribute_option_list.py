# core/classifications/attributes/ui/pages/attribute_options/attribute_option_list.py

from core.ui.registry import register_ui_module_pages
from ._base_attribute_option_list import build_attribute_option_list_page

UI_PAGES = build_attribute_option_list_page(
    key="attribute.options.list",
    domain="core",
    path="/settings/classifications/attributes/{attribute_id}/options",
    data_source="/entities/core/attribute_options.list/query/",
    permissions=["core.attributes.view"],
    create_path="/settings/classifications/attributes/{attribute_id}/options/create",
    edit_path="/settings/classifications/attributes/{attribute_id}/options/{id}/edit",
    delete_endpoint="/attribute-options/{id}/",
)

register_ui_module_pages("core", UI_PAGES)