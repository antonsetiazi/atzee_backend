# verticals/bengkel/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode

# 🔥 Owner (Full Control)
register_user_seed({
    "email": "owner@bengkel.com",
    "full_name": "Bengkel Owner",
    "password": "Owner123!",
    "tenant_code": "bengkel",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.OWNER
})


# 🛠 Service Advisor
register_user_seed({
    "email": "advisor@bengkel.com",
    "full_name": "Service Advisor",
    "password": "Advisor123!", 
    "tenant_code": "bengkel",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADVISOR
})


# 🔧 Mechanic
register_user_seed({
    "email": "mechanic@bengkel.com",
    "full_name": "Workshop Mechanic",
    "password": "Mechanic123!",
    "tenant_code": "bengkel",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.TECHNICIAN
})


# 💰 Cashier
register_user_seed({
    "email": "cashier@bengkel.com",
    "full_name": "Workshop Cashier",
    "password": "Cashier123!",
    "tenant_code": "bengkel",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.CASHIER
})