# core/classifications/tags/ui/pages/tag_create.py

from core.classifications.tags.ui.pages._base_tag_form import build_tag_form_page

UI_PAGES = build_tag_form_page(
    key="tags.create",
    domain="core",
    path="/settings/classifications/tags/create",
    submit_to="/tags/",
    method="POST",
    permissions=["core.tags.add"],
    title="Create Tag",
    redirect_page="/settings/classifications/tags",
)
