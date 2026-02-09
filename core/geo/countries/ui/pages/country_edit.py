# core/geo/countries/ui/pages/country_edit.py

from core.ui.schema.field import Field
from core.geo.countries.ui.pages._base_country_form import (
    build_country_form_page,
)

UI_PAGES = build_country_form_page(
    key="countries.edit",
    domain="core",
    path="/settings/geo/countries/:id/edit",
    submit_to="/countries/{id}/",
    method="PATCH",
    permissions=["core.countries.update"],
    title="Edit Country",
    redirect_page="/settings/geo/countries",
    extra_fields=[
        Field(key="id", label="Country ID", type="hidden"),
    ],
)
