# core/master/locations/ui/pages/location_create.py

from core.master.locations.ui.pages._base_location_form import (
    build_location_form_page,
)

UI_PAGES = build_location_form_page(
    key="locations.create",
    domain="core",
    path="/settings/master/location/create",
    submit_to="/locations/",
    method="POST",
    permissions=["core.location.add"],
    title="Create Location",
    redirect_page="/settings/master/location",
)
