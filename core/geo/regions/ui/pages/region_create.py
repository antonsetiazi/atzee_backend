# core/geo/regions/ui/pages/region_create.py

from core.geo.regions.ui.pages._base_region_form import (
    build_region_form_page,
)

UI_PAGES = build_region_form_page(
    key="regions.create",
    domain="core",
    path="/settings/geo/regions/create",
    submit_to="/regions/",
    method="POST",
    permissions=["core.regions.add"],
    title="Create Region",
    redirect_page="/settings/geo/regions",
)
