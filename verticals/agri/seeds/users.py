# verticals/agri/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode


# 👑 OWNER (Strategic Level)
register_user_seed({
    "email": "owner@agri.local",
    "full_name": "Agri Owner",
    "password": "Owner123!",
    "tenant_code": "agri",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.OWNER
})


# 🚜 FARM MANAGER (Operational Control)
register_user_seed({
    "email": "manager@agri.local",
    "full_name": "Farm Manager",
    "password": "Manager123!",
    "tenant_code": "agri",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.MANAGER
})


# 👨‍🌾 FIELD SUPERVISOR (Field Monitoring)
register_user_seed({
    "email": "supervisor@agri.local",
    "full_name": "Field Supervisor",
    "password": "Supervisor123!",
    "tenant_code": "agri",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.SUPERVISOR
})


# 👷 WORKER (Field Execution)
register_user_seed({
    "email": "worker@agri.local",
    "full_name": "Field Worker",
    "password": "Worker123!",
    "tenant_code": "agri",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.STAFF
})


# 💰 FINANCE (Agriculture Finance Officer)
register_user_seed({
    "email": "finance@agri.local",
    "full_name": "Finance Officer",
    "password": "Finance123!",
    "tenant_code": "agri",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.FINANCE
})