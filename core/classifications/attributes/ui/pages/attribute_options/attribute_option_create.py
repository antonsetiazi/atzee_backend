# core/classifications/attributes/ui/pages/attribute_options/attribute_option_create.py

from core.ui.registry import register_ui_module_pages
from ._base_attribute_option_form import build_attribute_option_form_page

UI_PAGES = build_attribute_option_form_page(
    key="attribute.options.create",
    domain="core",
    path="/settings/classifications/attributes/:attribute_id/options/create",
    submit_to="/attributes/{parent_id}/options/",
    method="POST",
    permissions=["core.attributes.add"],
    title="Create Attribute Option",
    redirect_page="/settings/classifications/attributes/:parent_id/edit",
    attribute_id="{parent_id}",
)

register_ui_module_pages("core", UI_PAGES)