# verticals/research/seeds/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
from verticals.research.enum.permissions import ResearchPermission
from core.roles.enums import RoleCode


ROLES = [

    # 🔥 Research Director (Full Vertical Control)
    {
        "code": RoleCode.OWNER,
        "name": "Research Director",
        "description": "Full control over research vertical including governance and funding",
        "access_level": 100,
        "auto_assign": "owner",
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Research Governance
            ResearchPermission.DIRECTOR_DASHBOARD_VIEW,
        ],
    },


    # 🏛 Committee Member (Approval Authority)
    {
        "code": RoleCode.DIRECTOR,
        "name": "Committee Member",
        "description": "Review and approve research proposals",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            ResearchPermission.COMMITTEE_DASHBOARD_VIEW,
        ],
    },


    # 🧪 Reviewer
    {
        "code": RoleCode.SUPERVISOR,
        "name": "Reviewer",
        "description": "Review assigned research proposals",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            ResearchPermission.REVIEWER_DASHBOARD_VIEW,
        ],
    },


    # 👨‍🔬 Principal Investigator (Project Owner)
    {
        "code": RoleCode.MANAGER,
        "name": "Principal Investigator",
        "description": "Lead research projects and manage team",
        "access_level": 75,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            ResearchPermission.PI_DASHBOARD_VIEW,
        ],
    },


    # 🔬 Researcher
    {
        "code": RoleCode.CUSTOMER,
        "name": "Researcher",
        "description": "Execute research tasks and update progress",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            ResearchPermission.RESEARCHER_DASHBOARD_VIEW,
        ],
    },


    # 🧾 Research Assistant
    {
        "code": RoleCode.STAFF,
        "name": "Research Assistant",
        "description": "Support research documentation and logistics",
        "access_level": 50,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            ResearchPermission.ASSISTANT_DASHBOARD_VIEW,
        ],
    },


    # 💰 Finance Officer
    {
        "code": RoleCode.FINANCE,
        "name": "Finance Officer",
        "description": "Manage and monitor research budgets",
        "access_level": 65,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            ResearchPermission.FINANCE_DASHBOARD_VIEW,
        ],
    },


    # 🛠 Admin (Operational System Admin)
    {
        "code": RoleCode.ADMIN,
        "name": "Admin",
        "description": "Manage operational system and user setup",
        "access_level": 85,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            ResearchPermission.ADMIN_DASHBOARD_VIEW,
        ],
    },
]