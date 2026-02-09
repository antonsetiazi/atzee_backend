# core/classifications/tags/ui/pages/tag_edit.py

from core.ui.schema.field import Field
from core.classifications.tags.ui.pages._base_tag_form import build_tag_form_page

UI_PAGES = build_tag_form_page(
    key="tags.edit",
    domain="core",
    path="/settings/classifications/tags/:id/edit",
    submit_to="/tags/{id}/",
    method="PATCH",
    permissions=["core.tags.update"],
    title="Edit Tag",
    redirect_page="/settings/classifications/tags",
    extra_fields=[
        Field(
            key="id", 
            label="Tag ID", 
            type="hidden"
        )
    ],
)
