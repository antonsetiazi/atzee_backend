# core/geo/ui/seed_menus.py

from core.geo.ui.menus import UI_MENUS as GEO_MENUS
from core.geo.countries.ui.menus import UI_MENUS as COUNTRY_MENUS
from core.geo.regions.ui.menus import UI_MENUS as REGION_MENUS
from core.geo.timezones.ui.menus import UI_MENUS as TIMEZONE_MENUS


UI_MENUS = (
    GEO_MENUS +
    COUNTRY_MENUS + 
    REGION_MENUS +
    TIMEZONE_MENUS
)
