# verticals/koperasi/seeds/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
from verticals.koperasi.enum.permissions import KoperasiPermission


ROLES = [

    # 👑 KETUA (Full Governance Control)
    {
        "name": "Ketua",
        "description": "Full governance control over koperasi operations",
        "access_level": 100,
        "auto_assign": "owner",
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            KoperasiPermission.KETUA_DASHBOARD_VIEW,
        ],
    },


    # 💰 BENDAHARA (Finance Operations)
    {
        "name": "Bendahara",
        "description": "Manage financial operations of koperasi",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            KoperasiPermission.BENDAHARA_DASHBOARD_VIEW,
        ],
    },


    # 🕵️ PENGAWAS (Audit Only)
    {
        "name": "Pengawas",
        "description": "Audit and monitor koperasi activities",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            KoperasiPermission.PENGAWAS_DASHBOARD_VIEW,
        ],
    },


    # 🧑‍💼 STAFF (Operational Input)
    {
        "name": "Staff",
        "description": "Handle daily koperasi operations",
        "access_level": 50,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            KoperasiPermission.STAFF_DASHBOARD_VIEW,
        ],
    },


    # 👤 MEMBER (Self-Service Only)
    {
        "name": "Member",
        "description": "Koperasi member with personal access only",
        "access_level": 10,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            KoperasiPermission.MEMBER_DASHBOARD_VIEW,
        ],
    },

]