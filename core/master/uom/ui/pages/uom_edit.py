# core/master/uom/ui/pages/uom_edit.py

from core.ui.schema.field import Field
from core.master.uom.ui.pages._base_uom_form import (
    build_uom_form_page,
)

UI_PAGES = build_uom_form_page(
    key="uom.edit",
    domain="core",
    path="/settings/master/uom/:id/edit",
    submit_to="/core/uoms/{id}/",
    method="PATCH",
    permissions=["core.uom.update"],
    title="Edit Unit of Measure",
    redirect_page="/settings/master/uom",
    extra_fields=[
        Field(key="id", label="UOM ID", type="hidden"),
    ],
)
