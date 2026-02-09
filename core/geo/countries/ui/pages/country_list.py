# core/geo/countries/ui/pages/country_list.py

from core.geo.countries.ui.pages._base_country_list import (
    build_country_list_page,
)

UI_PAGES = build_country_list_page(
    key="countries.list",
    domain="core",
    path="/settings/geo/countries",
    data_source="/entities/core/countries.list/query/",
    permissions=["core.countries.view"],
    create_path="/settings/geo/countries/create",
    edit_path="/settings/geo/countries/{id}/edit",
    delete_endpoint="/countries/{id}/",
)
