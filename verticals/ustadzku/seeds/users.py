# verticals/ustadzku/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode

# 🔹 Admin
register_user_seed({
    "email": "admin@ustadzku.com",
    "full_name": "Ustadzku Admin",
    "password": "Admin123!",
    "tenant_code": "ustadzku",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADMIN
})

# 🔹 Partner / Seller
register_user_seed({
    "email": "partner@ustadzku.com",
    "full_name": "Ustadzku Partner",
    "password": "Partner123!",
    "tenant_code": "ustadzku",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.PARTNER
})

# 🔹 Customer / Pelanggan
register_user_seed({
    "email": "customer@ustadzku.com",
    "full_name": "Ustadzku Customer",
    "password": "Customer123!",
    "tenant_code": "ustadzku",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.CUSTOMER
})
