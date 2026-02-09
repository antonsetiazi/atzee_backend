# core/geo/timezones/ui/pages/timezone_create.py

from core.geo.timezones.ui.pages._base_timezone_form import (
    build_timezone_form_page,
)

UI_PAGES = build_timezone_form_page(
    key="timezones.create",
    domain="core",
    path="/settings/geo/timezones/create",
    submit_to="/timezones/",
    method="POST",
    permissions=["core.timezones.add"],
    title="Create Timezone",
    redirect_page="/settings/geo/timezones",
)
