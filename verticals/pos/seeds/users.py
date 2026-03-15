# verticals/pos/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode


# 🔹 Tenant Owner (Superuser Lokal Tenant)
register_user_seed({
    "email": "owner@pos.com",
    "full_name": "POS Owner",
    "password": "Owner123!",
    "tenant_code": "pos",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.OWNER
})


# 🔹 Store Manager
register_user_seed({
    "email": "manager@pos.com",
    "full_name": "POS Store Manager",
    "password": "Manager123!",
    "tenant_code": "pos",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.MANAGER
})


# 🔹 Shift Supervisor
register_user_seed({
    "email": "supervisor@pos.com",
    "full_name": "POS Shift Supervisor",
    "password": "Supervisor123!",
    "tenant_code": "pos",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.SUPERVISOR
})


# 🔹 Cashier
register_user_seed({
    "email": "cashier@pos.com",
    "full_name": "POS Cashier",
    "password": "Cashier123!",
    "tenant_code": "pos",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.CASHIER
})


# 🔹 Area Manager (Multi Outlet Monitor)
register_user_seed({
    "email": "area@pos.com",
    "full_name": "POS Area Manager",
    "password": "Area123!",
    "tenant_code": "pos",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.MANAGER
})