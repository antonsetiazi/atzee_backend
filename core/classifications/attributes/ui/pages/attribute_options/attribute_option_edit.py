# core/classifications/attributes/ui/pages/attribute_options/attribute_option_edit.py

from core.ui.schema.field import Field
from ._base_attribute_option_form import build_attribute_option_form_page

UI_PAGES = build_attribute_option_form_page(
    key="attribute.options.edit",
    domain="core",
    path="/settings/classifications/attributes/:attribute_id/options/:id/edit",
    submit_to="/attributes/{parent_id}/options/{id}/",
    method="PATCH",
    permissions=["core.attributes.update"],
    title="Edit Attribute Option",
    redirect_page="/settings/classifications/attributes/:parent_id/edit",
    attribute_id="{parent_id}",
    extra_fields=[
        Field(key="id", label="ID", type="hidden"),
    ],
)

