# core/classifications/labels/ui/pages/label_create.py

from core.classifications.labels.ui.pages._base_label_form import build_label_form_page

UI_PAGES = build_label_form_page(
    key="labels.create",
    domain="core",
    path="/settings/classifications/labels/create",
    submit_to="/labels/",
    method="POST",
    permissions=["core.labels.add"],
    title="Create Label",
    redirect_page="/settings/classifications/labels",
)
