# verticals/koperasi/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode

# 👑 Ketua
register_user_seed({
    "email": "ketua@koperasi.com",
    "full_name": "Ketua Koperasi",
    "password": "Ketua123!",
    "tenant_code": "koperasi",
    "is_superuser": False,
    "is_staff": True,
    "role": "Ketua",
    "role_code": RoleCode.DIRECTOR
})


# 💰 Bendahara
register_user_seed({
    "email": "bendahara@koperasi.com",
    "full_name": "Bendahara Koperasi",
    "password": "Bendahara123!",
    "tenant_code": "koperasi",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.FINANCE
})


# 🕵️ Pengawas
register_user_seed({
    "email": "pengawas@koperasi.com",
    "full_name": "Pengawas Koperasi",
    "password": "Pengawas123!",
    "tenant_code": "koperasi",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADVISOR
})


# 🧑‍💼 Staff
register_user_seed({
    "email": "staff@koperasi.com",
    "full_name": "Staff Operasional",
    "password": "Staff123!",
    "tenant_code": "koperasi",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.STAFF
})


# 👤 Member
register_user_seed({
    "email": "member@koperasi.com",
    "full_name": "Anggota Koperasi",
    "password": "Member123!",
    "tenant_code": "koperasi",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.CUSTOMER
})