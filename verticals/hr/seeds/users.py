# verticals/hr/seeds/users.py

from core.roles.enums import RoleCode
from core.users.seed_registry import register_user_seed

# 🔹 Admin
register_user_seed(
    {
        "email": "admin@hr.com",
        "full_name": "HR Admin",
        "password": "Admin123!",
        "tenant_code": "hr",
        "is_superuser": False,
        "is_staff": True,
        "role_code": RoleCode.ADMIN,
    }
)
