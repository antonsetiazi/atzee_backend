# core/geo/ui/seed_pages.py

from core.geo.countries.ui.pages import UI_PAGES as COUNTRY_PAGES
from core.geo.regions.ui.pages import UI_PAGES as REGION_PAGES 
from core.geo.timezones.ui.pages import UI_PAGES as TIMEZONE_PAGES

UI_PAGES = [
    *COUNTRY_PAGES,
    *REGION_PAGES,
    *TIMEZONE_PAGES
]
