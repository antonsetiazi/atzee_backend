# verticals/cbs/seeds/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.cbs.enum.permissions import CbsPermission


ROLES = [

    # 🏦 Director (Full Tenant Control)
    {
        "name": "Director",
        "description": "Full control over CBS operations across all branches",
        "access_level": 100,
        "auto_assign": "director",
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # CBS
            CbsPermission.DIRECTOR_DASHBOARD_VIEW,
        ],
    },


    # 🏢 Branch Manager
    {
        "name": "Branch Manager",
        "description": "Manage branch operations, loans, and staff",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # CBS
            CbsPermission.BRANCH_MANAGER_DASHBOARD_VIEW,
        ],
    },


    # 📊 Credit Officer
    {
        "name": "Credit Officer",
        "description": "Analyze and process loan applications",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            CbsPermission.CREDIT_OFFICER_DASHBOARD_VIEW,
        ],
    },


    # 💵 Teller
    {
        "name": "Teller",
        "description": "Handle daily customer transactions",
        "access_level": 40,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            CbsPermission.TELLER_DASHBOARD_VIEW,
        ],
    },


    # 🧾 Back Office
    {
        "name": "Back Office",
        "description": "Reconciliation and operational verification",
        "access_level": 55,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            CbsPermission.BACK_OFFICE_DASHBOARD_VIEW,
        ],
    },


    # 🛡 Compliance Officer
    {
        "name": "Compliance Officer",
        "description": "Monitor AML, risk and regulatory compliance",
        "access_level": 75,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            CbsPermission.COMPLIANCE_DASHBOARD_VIEW,
        ],
    },


    # 🔎 Auditor (Read Only)
    {
        "name": "Auditor",
        "description": "Read-only access for auditing purposes",
        "access_level": 50,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            CbsPermission.AUDITOR_DASHBOARD_VIEW,
        ],
    },
]