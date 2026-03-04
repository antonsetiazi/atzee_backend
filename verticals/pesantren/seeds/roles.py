# verticals/pesantren/seed/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
from verticals.pesantren.enum.permissions import PesantrenPermission


ROLES = [

    # 🔥 OWNER (Full Control)
    {
        "name": "Owner",
        "description": "Full control over pesantren system",
        "access_level": 100,
        "auto_assign": "owner",
    },

    # 🏛 MUDHIR (Director)
    {
        "name": "Mudhir",
        "description": "Oversee academic, tahfidz, and discipline operations",
        "access_level": 90,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            PesantrenPermission.MUDHIR_DASHBOARD_VIEW,
        ],
    },

    # 💰 BENDAHARA
    {
        "name": "Bendahara",
        "description": "Manage pesantren financial operations",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            PesantrenPermission.BENDAHARA_DASHBOARD_VIEW,
        ],
    },

    # 🧾 STAFF ADMIN
    {
        "name": "Staff Admin",
        "description": "Handle santri administration and registration",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            PesantrenPermission.STAFF_ADMIN_DASHBOARD_VIEW,
        ],
    },

    # 📚 USTADZ
    {
        "name": "Ustadz",
        "description": "Teach classes and manage academic records",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            PesantrenPermission.USTADZ_DASHBOARD_VIEW,
        ],
    },

    # 🕌 MUSYRIF (Dorm Supervisor)
    {
        "name": "Musyrif",
        "description": "Supervise dormitory and student discipline",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            PesantrenPermission.MUSYRIF_DASHBOARD_VIEW,
        ],
    },

    # 👨‍👩‍👧 WALI SANTRI
    {
        "name": "Wali Santri",
        "description": "Monitor child academic and financial progress",
        "access_level": 30,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            PesantrenPermission.WALI_DASHBOARD_VIEW,
        ],
    },

    # 🧑‍🎓 SANTRI
    {
        "name": "Santri",
        "description": "Access personal academic and tahfidz data",
        "access_level": 20,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            PesantrenPermission.SANTRI_DASHBOARD_VIEW,
        ],
    },

]