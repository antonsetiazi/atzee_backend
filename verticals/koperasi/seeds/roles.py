# verticals/koperasi/seeds/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
# from verticals.koperasi.enum.permissions import KoperasiPermission


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

            # # Members
            # KoperasiPermission.MEMBER_VIEW,
            # KoperasiPermission.MEMBER_CREATE,
            # KoperasiPermission.MEMBER_APPROVE,

            # # Savings
            # KoperasiPermission.SAVINGS_VIEW,
            # KoperasiPermission.SAVINGS_CREATE,

            # # Loans
            # KoperasiPermission.LOAN_VIEW,
            # KoperasiPermission.LOAN_CREATE,
            # KoperasiPermission.LOAN_APPROVE,

            # # SHU
            # KoperasiPermission.SHU_VIEW,
            # KoperasiPermission.SHU_GENERATE,
            # KoperasiPermission.SHU_APPROVE,

            # # RAT
            # KoperasiPermission.RAT_VIEW,
            # KoperasiPermission.RAT_MANAGE,

            # # Reports & Settings
            # KoperasiPermission.REPORT_VIEW,
            # KoperasiPermission.SETTINGS_MANAGE,
        ],
    },


    # 💰 BENDAHARA (Finance Operations)
    {
        "name": "Bendahara",
        "description": "Manage financial operations of koperasi",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # # Members (view only)
            # KoperasiPermission.MEMBER_VIEW,

            # # Savings
            # KoperasiPermission.SAVINGS_VIEW,
            # KoperasiPermission.SAVINGS_CREATE,

            # # Loans
            # KoperasiPermission.LOAN_VIEW,
            # KoperasiPermission.LOAN_CREATE,

            # # SHU
            # KoperasiPermission.SHU_VIEW,
            # KoperasiPermission.SHU_GENERATE,

            # # Reports
            # KoperasiPermission.REPORT_VIEW,
        ],
    },


    # 🕵️ PENGAWAS (Audit Only)
    {
        "name": "Pengawas",
        "description": "Audit and monitor koperasi activities",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # KoperasiPermission.MEMBER_VIEW,
            # KoperasiPermission.SAVINGS_VIEW,
            # KoperasiPermission.LOAN_VIEW,
            # KoperasiPermission.SHU_VIEW,
            # KoperasiPermission.RAT_VIEW,
            # KoperasiPermission.REPORT_VIEW,
        ],
    },


    # 🧑‍💼 STAFF (Operational Input)
    {
        "name": "Staff",
        "description": "Handle daily koperasi operations",
        "access_level": 50,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # # Members
            # KoperasiPermission.MEMBER_VIEW,
            # KoperasiPermission.MEMBER_CREATE,

            # # Savings
            # KoperasiPermission.SAVINGS_VIEW,
            # KoperasiPermission.SAVINGS_CREATE,

            # # Loans
            # KoperasiPermission.LOAN_VIEW,
            # KoperasiPermission.LOAN_CREATE,
        ],
    },


    # 👤 MEMBER (Self-Service Only)
    {
        "name": "Member",
        "description": "Koperasi member with personal access only",
        "access_level": 10,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # KoperasiPermission.MY_SAVINGS_VIEW,
            # KoperasiPermission.MY_LOAN_VIEW,
            # KoperasiPermission.MY_SHU_VIEW,
            # KoperasiPermission.MY_STATEMENT_VIEW,
        ],
    },

]