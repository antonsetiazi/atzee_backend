# verticals/distributor/seeds/users.py

# verticals/distributor/seeds/users.py

from core.users.seed_registry import register_user_seed


# ==========================================================
# 🔹 EXECUTIVE LEVEL
# ==========================================================

# Owner / Director
register_user_seed({
    "email": "owner@distributor.com",
    "full_name": "Distributor Owner",
    "password": "Owner123!",
    "tenant_code": "distributor",
    "is_superuser": True,
    "is_staff": True,
    "role": "Owner",
})


# ==========================================================
# 🔹 MANAGERIAL LEVEL
# ==========================================================

# General Manager
register_user_seed({
    "email": "gm@distributor.com",
    "full_name": "General Manager",
    "password": "GM123!",
    "tenant_code": "distributor",
    "is_superuser": False,
    "is_staff": True,
    "role": "General Manager",
})

# Sales Manager
register_user_seed({
    "email": "sales.manager@distributor.com",
    "full_name": "Sales Manager",
    "password": "SalesManager123!",
    "tenant_code": "distributor",
    "is_superuser": False,
    "is_staff": True,
    "role": "Sales Manager",
})

# Warehouse Manager
register_user_seed({
    "email": "warehouse.manager@distributor.com",
    "full_name": "Warehouse Manager",
    "password": "WarehouseManager123!",
    "tenant_code": "distributor",
    "is_superuser": False,
    "is_staff": True,
    "role": "Warehouse Manager",
})

# Finance Manager
register_user_seed({
    "email": "finance.manager@distributor.com",
    "full_name": "Finance Manager",
    "password": "FinanceManager123!",
    "tenant_code": "distributor",
    "is_superuser": False,
    "is_staff": True,
    "role": "Finance Manager",
})


# ==========================================================
# 🔹 OPERATIONAL LEVEL
# ==========================================================

# Sales Rep (Field Sales)
register_user_seed({
    "email": "sales.rep@distributor.com",
    "full_name": "Sales Representative",
    "password": "SalesRep123!",
    "tenant_code": "distributor",
    "is_superuser": False,
    "is_staff": False,
    "role": "Sales Rep",
})

# Admin Sales
register_user_seed({
    "email": "admin.sales@distributor.com",
    "full_name": "Admin Sales",
    "password": "AdminSales123!",
    "tenant_code": "distributor",
    "is_superuser": False,
    "is_staff": True,
    "role": "Admin Sales",
})

# Warehouse Staff
register_user_seed({
    "email": "warehouse.staff@distributor.com",
    "full_name": "Warehouse Staff",
    "password": "WarehouseStaff123!",
    "tenant_code": "distributor",
    "is_superuser": False,
    "is_staff": True,
    "role": "Warehouse Staff",
})

# Finance Staff
register_user_seed({
    "email": "finance.staff@distributor.com",
    "full_name": "Finance Staff",
    "password": "FinanceStaff123!",
    "tenant_code": "distributor",
    "is_superuser": False,
    "is_staff": True,
    "role": "Finance Staff",
})