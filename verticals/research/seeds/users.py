# verticals/research/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode


# =========================================================
# 🔹 System Admin (Operational / Technical)
# =========================================================
register_user_seed({
    "email": "admin@research.com",
    "full_name": "Research System Admin",
    "password": "Admin123!",
    "tenant_code": "research",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADMIN
})


# =========================================================
# 🔹 Research Director (Full Vertical Control)
# =========================================================
register_user_seed({
    "email": "director@research.com",
    "full_name": "Research Director",
    "password": "Director123!",
    "tenant_code": "research",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.DIRECTOR
})


# =========================================================
# 🔹 Committee Member (Governance & Approval)
# =========================================================
register_user_seed({
    "email": "committee@research.com",
    "full_name": "Committee Member",
    "password": "Committee123!",
    "tenant_code": "research",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.SUPERVISOR
})


# =========================================================
# 🔹 Reviewer (Proposal Review)
# =========================================================
register_user_seed({
    "email": "reviewer@research.com",
    "full_name": "Research Reviewer",
    "password": "Reviewer123!",
    "tenant_code": "research",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.VIEWER
})


# =========================================================
# 🔹 Principal Investigator (Project Leader)
# =========================================================
register_user_seed({
    "email": "pi@research.com",
    "full_name": "Principal Investigator",
    "password": "PI123!",
    "tenant_code": "research",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.SUPERVISOR
})


# =========================================================
# 🔹 Researcher (Execution Level)
# =========================================================
register_user_seed({
    "email": "researcher@research.com",
    "full_name": "Researcher User",
    "password": "Researcher123!",
    "tenant_code": "research",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.CUSTOMER
})


# =========================================================
# 🔹 Research Assistant (Support)
# =========================================================
register_user_seed({
    "email": "assistant@research.com",
    "full_name": "Research Assistant",
    "password": "Assistant123!",
    "tenant_code": "research",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.CUSTOMER
})


# =========================================================
# 🔹 Finance Officer (Budget Control)
# =========================================================
register_user_seed({
    "email": "finance@research.com",
    "full_name": "Finance Officer",
    "password": "Finance123!",
    "tenant_code": "research",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.FINANCE
})