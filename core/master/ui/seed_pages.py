# core/master/ui/seed_pages.py

from core.master.uom.ui.pages import UI_PAGES as UOM_PAGES
from core.master.locations.ui.pages import UI_PAGES as LOCATION_PAGES 
from core.master.currencies.ui.pages import UI_PAGES as CURRENCY_PAGES

UI_PAGES = [
    *UOM_PAGES,
    *LOCATION_PAGES,
    *CURRENCY_PAGES
]
