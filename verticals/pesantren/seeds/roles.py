# verticals/pesantren/seed/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
# from verticals.pesantren.enum.permissions import PesantrenPermission


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

            # # Pesantren
            # PesantrenPermission.SANTRI_VIEW,
            # PesantrenPermission.AKADEMIK_VIEW,
            # PesantrenPermission.TAHFIDZ_VIEW,
            # PesantrenPermission.DISIPLIN_VIEW,
            # PesantrenPermission.REPORT_VIEW,

            # # Business (read-only style)
            # BusinessPermission.REPORT_VIEW,
        ],
    },

    # 💰 BENDAHARA
    {
        "name": "Bendahara",
        "description": "Manage pesantren financial operations",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # # Pesantren Financial
            # PesantrenPermission.KEUANGAN_VIEW,
            # PesantrenPermission.KEUANGAN_MANAGE,
            # PesantrenPermission.DONATUR_VIEW,

            # # Business Accounting
            # BusinessPermission.ACCOUNTING_VIEW,
            # BusinessPermission.TRANSACTION_VIEW,
            # BusinessPermission.TRANSACTION_CREATE,
        ],
    },

    # 🧾 STAFF ADMIN
    {
        "name": "Staff Admin",
        "description": "Handle santri administration and registration",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # PesantrenPermission.SANTRI_VIEW,
            # PesantrenPermission.SANTRI_CREATE,
            # PesantrenPermission.SANTRI_UPDATE,

            # PesantrenPermission.PERIZINAN_VIEW,
            # PesantrenPermission.PERIZINAN_PROCESS,

            # PesantrenPermission.KEUANGAN_VIEW,
        ],
    },

    # 📚 USTADZ
    {
        "name": "Ustadz",
        "description": "Teach classes and manage academic records",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # PesantrenPermission.AKADEMIK_VIEW,
            # PesantrenPermission.NILAI_INPUT,
            # PesantrenPermission.ABSENSI_INPUT,

            # PesantrenPermission.TAHFIDZ_VIEW,
        ],
    },

    # 🕌 MUSYRIF (Dorm Supervisor)
    {
        "name": "Musyrif",
        "description": "Supervise dormitory and student discipline",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # PesantrenPermission.ASRAMA_VIEW,
            # PesantrenPermission.ABSENSI_ASRAMA_INPUT,

            # PesantrenPermission.DISIPLIN_VIEW,
            # PesantrenPermission.DISIPLIN_CREATE,

            # PesantrenPermission.PERIZINAN_VIEW,
            # PesantrenPermission.PERIZINAN_APPROVE,
        ],
    },

    # 👨‍👩‍👧 WALI SANTRI
    {
        "name": "Wali Santri",
        "description": "Monitor child academic and financial progress",
        "access_level": 30,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # PesantrenPermission.PORTAL_VIEW,
            # PesantrenPermission.NILAI_VIEW,
            # PesantrenPermission.TAHFIDZ_VIEW,
            # PesantrenPermission.KEUANGAN_VIEW,
            # PesantrenPermission.PERIZINAN_CREATE,
        ],
    },

    # 🧑‍🎓 SANTRI
    {
        "name": "Santri",
        "description": "Access personal academic and tahfidz data",
        "access_level": 20,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # PesantrenPermission.PORTAL_VIEW,
            # PesantrenPermission.JADWAL_VIEW,
            # PesantrenPermission.NILAI_VIEW,
            # PesantrenPermission.TAHFIDZ_VIEW,
            # PesantrenPermission.PERIZINAN_CREATE,
        ],
    },

]