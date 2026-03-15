# verticals/marketplace/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode

# 🔹 Marketplace Admin
register_user_seed({
    "email": "admin@marketplace.com",
    "full_name": "Marketplace Admin",
    "password": "Admin123!",
    "tenant_code": "marketplace",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADMIN
})


# 🔹 Marketplace Seller
register_user_seed({
    "email": "seller@marketplace.com",
    "full_name": "Marketplace Seller",
    "password": "Seller123!",
    "tenant_code": "marketplace",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.PARTNER
})


# 🔹 Marketplace Buyer
register_user_seed({
    "email": "buyer@marketplace.com",
    "full_name": "Marketplace Buyer",
    "password": "Buyer123!",
    "tenant_code": "marketplace",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.CUSTOMER
})