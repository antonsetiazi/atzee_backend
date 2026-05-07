# verticals/finance/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode

# 🔹 Admin
register_user_seed({
    "email": "admin@finance.com",
    "full_name": "Finance Admin",
    "password": "Admin123!",
    "tenant_code": "finance",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADMIN
})