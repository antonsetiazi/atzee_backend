# verticals/marketplace/enum/permissions.py

from enum import Enum

class MarketplacePermission(str, Enum):

    BUYER_DASHBOARD_VIEW = "marketplace.buyer.dashboard.view"
    SELLER_DASHBOARD_VIEW = "marketplace.seller.dashboard.view"
    ADMIN_DASHBOARD_VIEW = "marketplace.admin.dashboard.view"


    def __str__(self):
        return self.value