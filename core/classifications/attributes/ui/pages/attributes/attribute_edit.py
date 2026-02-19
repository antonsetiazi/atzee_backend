# core/classifications/attributes/ui/pages/attributes/attribute_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from ._base_attribute_form import (
    build_attribute_form_page,
)
from ._base_attribute_option_block import build_attribute_option_block


UI_PAGES = build_attribute_form_page(
    key="attributes.edit",
    domain="core",
    path="/settings/classifications/attributes/:id/edit",
    submit_to="/attributes/{id}/",
    method="PATCH",
    permissions=["core.attributes.update"],
    title="Edit Attribute",
    redirect_page="/settings/classifications/attributes",
    extra_fields=[
        Field(key="id", label="Attribute ID", type="hidden"),
    ],
    extra_blocks=[
        build_attribute_option_block(parent_id="{parent_id}"),
    ],
)

register_ui_module_pages("core", UI_PAGES)