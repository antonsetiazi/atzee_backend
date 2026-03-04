# verticals/isp/seeds/users.py

from core.users.seed_registry import register_user_seed


# 🔥 100 - Owner
register_user_seed({
    "email": "owner@isp.com",
    "full_name": "ISP Owner",
    "password": "Owner123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "Owner",
})


# 🏢 90 - General Manager
register_user_seed({
    "email": "gm@isp.com",
    "full_name": "ISP General Manager",
    "password": "Gm123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "General Manager",
})


# 💳 80 - Finance Manager
register_user_seed({
    "email": "finance@isp.com",
    "full_name": "ISP Finance Manager",
    "password": "Finance123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "Finance Manager",
})


# 🧠 70 - Network Engineer
register_user_seed({
    "email": "engineer@isp.com",
    "full_name": "ISP Network Engineer",
    "password": "Engineer123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "Network Engineer",
})


# 🖥 60 - NOC Staff
register_user_seed({
    "email": "noc@isp.com",
    "full_name": "ISP NOC Staff",
    "password": "Noc123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "NOC Staff",
})


# 💰 50 - Billing Staff
register_user_seed({
    "email": "billing@isp.com",
    "full_name": "ISP Billing Staff",
    "password": "Billing123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "Billing Staff",
})


# 📞 40 - Customer Service
register_user_seed({
    "email": "cs@isp.com",
    "full_name": "ISP Customer Service",
    "password": "Cs123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "Customer Service",
})


# 📈 30 - Sales Marketing
register_user_seed({
    "email": "sales@isp.com",
    "full_name": "ISP Sales Marketing",
    "password": "Sales123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "Sales Marketing",
})


# 🔧 20 - Field Technician
register_user_seed({
    "email": "technician@isp.com",
    "full_name": "ISP Field Technician",
    "password": "Technician123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": True,
    "role": "Field Technician",
})


# 🌐 10 - Customer (Self Portal)
register_user_seed({
    "email": "customer@isp.com",
    "full_name": "ISP Customer",
    "password": "Customer123!",
    "tenant_code": "isp",
    "is_superuser": False,
    "is_staff": False,
    "role": "Customer",
})