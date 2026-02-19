# core/master/locations/ui/pages/location_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from core.master.locations.ui.pages._base_location_form import (
    build_location_form_page,
)

UI_PAGES = build_location_form_page(
    key="locations.edit",
    domain="core",
    path="/settings/master/location/:id/edit",
    submit_to="/locations/{id}/",
    method="PATCH",
    permissions=["core.location.update"],
    title="Edit Location",
    redirect_page="/settings/master/location",
    extra_fields=[
        Field(
            key="id",
            label="Location ID",
            type="hidden",
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)