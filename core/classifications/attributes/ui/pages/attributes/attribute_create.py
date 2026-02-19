# core/classifications/attributes/ui/pages/attributes/attribute_create.py

from core.ui.registry import register_ui_module_pages
from ._base_attribute_form import (
    build_attribute_form_page,
)

UI_PAGES = build_attribute_form_page(
    key="attributes.create",
    domain="core",
    path="/settings/classifications/attributes/create",
    submit_to="/attributes/",
    method="POST",
    permissions=["core.attributes.add"],
    title="Create Attribute",
    redirect_page="/settings/classifications/attributes",
)

register_ui_module_pages("core", UI_PAGES)