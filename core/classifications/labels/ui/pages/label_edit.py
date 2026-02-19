# core/classifications/labels/ui/pages/label_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from core.classifications.labels.ui.pages._base_label_form import build_label_form_page

UI_PAGES = build_label_form_page(
    key="labels.edit",
    domain="core",
    path="/settings/classifications/labels/:id/edit",
    submit_to="/labels/{id}/",
    method="PATCH",
    permissions=["core.labels.update"],
    title="Edit Label",
    redirect_page="/settings/classifications/labels",
    extra_fields=[
        Field(key="id", label="Label ID", type="hidden"),
    ],
)

register_ui_module_pages("core", UI_PAGES)