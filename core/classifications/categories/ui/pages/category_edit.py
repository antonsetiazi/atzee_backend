# core/classifications/categories/ui/pages/category_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from core.classifications.categories.ui.pages._base_category_form import (
    build_category_form_page,
)

UI_PAGES = build_category_form_page(
    key="categories.edit",
    domain="core",
    path="/settings/classifications/categories/:id/edit",
    submit_to="/categories/{id}/",
    method="PATCH",
    permissions=["core.categories.update"],
    title="Edit Category",
    redirect_page="/settings/classifications/categories",
    extra_fields=[
        Field(key="id", label="Category ID", type="hidden"),
    ],
)

register_ui_module_pages("core", UI_PAGES)