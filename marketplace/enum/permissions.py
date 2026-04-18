# marketplace/enum/permissions.py

from enum import Enum

class MarketplacePermission(str, Enum):

    ADMIN_ORDERS_VIEW = "marketplace.admin.orders.view"
    PARTNER_PRODUCTS_VIEW = "marketplace.partner.products.view"
    PARTNER_PRODUCTS_EDIT = "marketplace.partner.products.edit"
    PARTNER_PRODUCTS_CREATE = "marketplace.partner.products.create"


    def __str__(self):
        return self.value