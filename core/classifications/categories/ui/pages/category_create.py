# core/classifications/categories/ui/pages/category_create.py

from core.classifications.categories.ui.pages._base_category_form import (
    build_category_form_page,
)

UI_PAGES = build_category_form_page(
    key="categories.create",
    domain="core",
    path="/settings/classifications/categories/create",
    submit_to="/categories/",
    method="POST",
    permissions=["core.categories.add"],
    title="Create Category",
    redirect_page="/settings/classifications/categories",
)
