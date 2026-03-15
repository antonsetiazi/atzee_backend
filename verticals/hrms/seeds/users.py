# verticals/hrms/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode


# 🔹 HR Administrator (Full Control HR)
register_user_seed({
    "email": "admin@hrms.com",
    "full_name": "HRMS Administrator",
    "password": "Admin123!",
    "tenant_code": "hrms",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADMIN
})


# 🔹 HR Officer (Operasional Harian)
register_user_seed({
    "email": "officer@hrms.com",
    "full_name": "HRMS Officer",
    "password": "Officer123!",
    "tenant_code": "hrms",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.STAFF
})


# 🔹 Line Manager (Atasan Langsung)
register_user_seed({
    "email": "manager@hrms.com",
    "full_name": "HRMS Line Manager",
    "password": "Manager123!",
    "tenant_code": "hrms",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.MANAGER
})


# 🔹 Employee (Self Service User)
register_user_seed({
    "email": "employee@hrms.com",
    "full_name": "HRMS Employee",
    "password": "Employee123!",
    "tenant_code": "hrms",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.STAFF
})


# 🔹 Finance Officer (Payroll & Journal)
register_user_seed({
    "email": "finance@hrms.com",
    "full_name": "HRMS Finance Officer",
    "password": "Finance123!",
    "tenant_code": "hrms",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.FINANCE
})


# 🔹 Executive (Read-Only Monitoring)
register_user_seed({
    "email": "executive@hrms.com",
    "full_name": "HRMS Executive",
    "password": "Executive123!",
    "tenant_code": "hrms",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.DIRECTOR
})