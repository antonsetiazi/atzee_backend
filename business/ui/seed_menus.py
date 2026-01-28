# business/ui/seed_menus.py

from business.customers.ui.menus import UI_MENUS as CUSTOMER_MENUS
from business.products.ui.menus import UI_MENUS as PRODUCT_MENUS
from business.partners.ui.menus import UI_MENUS as PARTNER_MENUS

UI_MENUS = (
    CUSTOMER_MENUS +
    PRODUCT_MENUS +
    PARTNER_MENUS
)
