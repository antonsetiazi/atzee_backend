# core/geo/regions/ui/pages/region_edit.py

from core.ui.schema.field import Field
from core.geo.regions.ui.pages._base_region_form import (
    build_region_form_page,
)

UI_PAGES = build_region_form_page(
    key="regions.edit",
    domain="core",
    path="/settings/geo/regions/:id/edit",
    submit_to="/regions/{id}/",
    method="PATCH",
    permissions=["core.regions.update"],
    title="Edit Region",
    redirect_page="/settings/geo/regions",
    extra_fields=[
        Field(key="id", label="Region ID", type="hidden"),
    ],
)
