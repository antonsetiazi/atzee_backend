# core/master/ui/seed_pages.py

from core.master.uom.ui.pages import UI_PAGES as UOM_PAGES
from core.master.locations.ui.pages import UI_PAGES as LOCATION_PAGES 
# from core.master.partners.ui.pages import UI_PAGES as PARTNER_PAGES
# from core.master.sales.ui.pages import UI_PAGES as SALES_PAGES
# from core.master.inventory.ui.pages import UI_PAGES as INVENTORY_PAGES

UI_PAGES = [
    *UOM_PAGES,
    *LOCATION_PAGES
    # *PRODUCT_PAGES,
    # *PARTNER_PAGES,
    # *SALES_PAGES,
    # *INVENTORY_PAGES,
]
