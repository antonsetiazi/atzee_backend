# business/enum/permissions.py

from enum import Enum

class BusinessPermission(str, Enum):

    ADMIN_BOOKINGS_VIEW = "business.admin.bookings.view"
    PARTNER_BOOKINGS_VIEW = "business.partner.bookings.view"
    USER_BOOKINGS_VIEW = "business.user.bookings.view"

    BOOKINGS_CREATE = "business.bookings.create"
    BOOKINGS_VIEW = "business.bookings.view"
    BOOKINGS_PAY = "business.bookings.pay"
    
    CUSTOMERS_VIEW = "business.customers.view"

    INVENTORY_VIEW = "business.inventory.view"
    
    PARTNERS_CREATE = "business.partners.create"
    PARTNERS_VIEW = "business.partners.view"
    PARTNERS_UPDATE = "business.partners.update"
    
    PRODUCTS_VIEW = "business.products.view"

    USERS_VIEW = "business.users.view"



    def __str__(self):
        return self.value