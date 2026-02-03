# business/ui/seed_menus.py

from business.ui.menus import UI_MENUS as BUSINESS_MENUS
from business.customers.ui.menus import UI_MENUS as CUSTOMER_MENUS
from business.partners.ui.menus import UI_MENUS as PARTNER_MENUS
from business.products.ui.menus import UI_MENUS as PRODUCT_MENUS
from business.sales.ui.menus import UI_MENUS as SALES_MENUS

UI_MENUS = (
    BUSINESS_MENUS +
    CUSTOMER_MENUS +
    PARTNER_MENUS +
    PRODUCT_MENUS +
    SALES_MENUS
)
