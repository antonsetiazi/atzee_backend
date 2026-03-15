# verticals/pesantren/seeds/users.py

from core.users.seed_registry import register_user_seed
from core.roles.enums import RoleCode


# 🔥 1️⃣ Owner Pesantren (Full Control)
register_user_seed({
    "email": "owner@pesantren.com",
    "full_name": "Owner Pesantren",
    "password": "Owner123!",
    "tenant_code": "pesantren",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.OWNER
})


# 🏛 2️⃣ Mudhir (Direktur Pesantren)
register_user_seed({
    "email": "mudhir@pesantren.com",
    "full_name": "Mudhir Pesantren",
    "password": "Mudhir123!",
    "tenant_code": "pesantren",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.DIRECTOR
})


# 💰 3️⃣ Bendahara
register_user_seed({
    "email": "bendahara@pesantren.com",
    "full_name": "Bendahara Pesantren",
    "password": "Bendahara123!",
    "tenant_code": "pesantren",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.FINANCE
})


# 🧾 4️⃣ Staff Administrasi
register_user_seed({
    "email": "admin@pesantren.com",
    "full_name": "Staff Administrasi",
    "password": "Admin123!",
    "tenant_code": "pesantren",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADMIN
})


# 📚 5️⃣ Ustadz
register_user_seed({
    "email": "ustadz@pesantren.com",
    "full_name": "Ustadz Pesantren",
    "password": "Ustadz123!",
    "tenant_code": "pesantren",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.STAFF
})


# 🕌 6️⃣ Musyrif
register_user_seed({
    "email": "musyrif@pesantren.com",
    "full_name": "Musyrif Asrama",
    "password": "Musyrif123!",
    "tenant_code": "pesantren",
    "is_superuser": False,
    "is_staff": True,
    "role_code": RoleCode.ADVISOR
})


# 👨‍👩‍👧 7️⃣ Wali Santri
register_user_seed({
    "email": "wali@pesantren.com",
    "full_name": "Wali Santri",
    "password": "Wali123!",
    "tenant_code": "pesantren",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.ADVISOR
})


# 🧑‍🎓 8️⃣ Santri
register_user_seed({
    "email": "santri@pesantren.com",
    "full_name": "Santri Pesantren",
    "password": "Santri123!",
    "tenant_code": "pesantren",
    "is_superuser": False,
    "is_staff": False,
    "role_code": RoleCode.CUSTOMER
})