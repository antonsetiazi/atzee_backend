# business/ui/seed_pages.py

from business.customers.ui.pages import UI_PAGES as CUSTOMER_PAGES
from business.products.ui.pages import UI_PAGES as PRODUCT_PAGES
from business.partners.ui.pages import UI_PAGES as PARTNER_PAGES
from business.sales.ui.pages import UI_PAGES as SALES_PAGES
from business.inventory.ui.pages import UI_PAGES as INVENTORY_PAGES

UI_PAGES = [
    *CUSTOMER_PAGES,
    *PRODUCT_PAGES,
    *PARTNER_PAGES,
    *SALES_PAGES,
    *INVENTORY_PAGES,
]
