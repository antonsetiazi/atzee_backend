# core/geo/countries/ui/pages/country_create.py

from core.geo.countries.ui.pages._base_country_form import (
    build_country_form_page,
)

UI_PAGES = build_country_form_page(
    key="countries.create",
    domain="core",
    path="/settings/geo/countries/create",
    submit_to="/countries/",
    method="POST",
    permissions=["core.countries.add"],
    title="Create Country",
    redirect_page="/settings/geo/countries",
)
