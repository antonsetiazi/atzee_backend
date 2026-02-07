# core/master/uom/ui/pages/uom_create.py

from core.master.uom.ui.pages._base_uom_form import (
    build_uom_form_page,
)

UI_PAGES = build_uom_form_page(
    key="uom.create",
    domain="core",
    path="/settings/master/uom/create",
    submit_to="/core/uoms/",
    method="POST",
    permissions=["core.uom.add"],
    title="Create Unit of Measure",
    redirect_page="/settings/master/uom",
)
