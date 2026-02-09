# core/geo/timezones/ui/pages/timezone_edit.py

from core.ui.schema.field import Field
from core.geo.timezones.ui.pages._base_timezone_form import (
    build_timezone_form_page,
)

UI_PAGES = build_timezone_form_page(
    key="timezones.edit",
    domain="core",
    path="/settings/geo/timezones/:id/edit",
    submit_to="/timezones/{id}/",
    method="PATCH",
    permissions=["core.timezones.update"],
    title="Edit Timezone",
    redirect_page="/settings/geo/timezones",
    extra_fields=[
        Field(key="id", label="Timezone ID", type="hidden"),
    ],
)
