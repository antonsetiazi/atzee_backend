# marketplace/enum/permissions.py

from enum import Enum

class MarketplacePermission(str, Enum):

    ADMIN_ORDERS_VIEW = "marketplace.admin.orders.view"


    def __str__(self):
        return self.value