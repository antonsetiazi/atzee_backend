# verticals/cbs/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode


# 🔹 Director (Full Control Tenant Level)
register_user_seed({
    "email": "director@cbs.com",
    "full_name": "CBS Director",
    "password": "Director123!",
    "tenant_code": "cbs",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.DIRECTOR
})


# 🔹 Branch Manager
register_user_seed({
    "email": "branch.manager@cbs.com",
    "full_name": "CBS Branch Manager",
    "password": "Branch123!",
    "tenant_code": "cbs",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.MANAGER
})


# 🔹 Credit Officer
register_user_seed({
    "email": "credit.officer@cbs.com",
    "full_name": "CBS Credit Officer",
    "password": "Credit123!",
    "tenant_code": "cbs",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.STAFF
})


# 🔹 Teller
register_user_seed({
    "email": "teller@cbs.com",
    "full_name": "CBS Teller",
    "password": "Teller123!",
    "tenant_code": "cbs",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.CASHIER
})


# 🔹 Back Office
register_user_seed({
    "email": "backoffice@cbs.com",
    "full_name": "CBS Back Office",
    "password": "BackOffice123!",
    "tenant_code": "cbs",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADMIN
})


# 🔹 Compliance Officer
register_user_seed({
    "email": "compliance@cbs.com",
    "full_name": "CBS Compliance Officer",
    "password": "Compliance123!",
    "tenant_code": "cbs",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADMIN
})


# 🔹 Auditor (Read Only)
register_user_seed({
    "email": "auditor@cbs.com",
    "full_name": "CBS Auditor",
    "password": "Auditor123!",
    "tenant_code": "cbs",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.VIEWER
})