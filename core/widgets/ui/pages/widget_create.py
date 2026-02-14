# core/widgets/ui/pages/widget_create.py

from core.widgets.ui.pages._base_widget_form import (
    build_widget_form_page,
)

UI_PAGES = build_widget_form_page(
    key="widgets.create",
    domain="core",
    path="/settings/widgets/create",
    title_page="Widget",
    submit_to="/widgets/",
    method="POST",
    permissions=["core.widgets.add"],
    title="Create Widget",
    widget_type="",
    redirect_page="/settings/widgets",
)
