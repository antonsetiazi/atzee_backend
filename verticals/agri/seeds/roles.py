# verticals/agri/seeds/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.agri.enum.permissions import AgriPermission
from core.roles.enums import RoleCode


ROLES = [

    # 🌾 Owner (Full Farm Control)
    {
        "code": RoleCode.OWNER,
        "name": "Owner",
        "description": "Farm owner with full operational and financial control",
        "access_level": 100,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Agri
            AgriPermission.OWNER_DASHBOARD_VIEW,
        ],
    },


    # 🚜 Farm Manager
    {
        "code": RoleCode.MANAGER,
        "name": "Farm Manager",
        "description": "Manage farm operations, crops, and workforce",
        "access_level": 85,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Agri
            AgriPermission.MANAGER_DASHBOARD_VIEW,
        ],
    },


    # # 🌱 Field Supervisor
    # {
    #     "code": RoleCode.,
    #     "name": "Field Supervisor",
    #     "description": "Supervise daily farming activities and workers",
    #     "access_level": 65,
    #     "default_permissions": [

    #         # Core
    #         CorePermission.DASHBOARD_VIEW,

    #         # Agri
    #         AgriPermission.SUPERVISOR_DASHBOARD_VIEW,
    #     ],
    # },


    # 👨‍🌾 Worker
    {
        "code": RoleCode.ADMIN,
        "name": "Worker",
        "description": "Execute daily farming tasks in the field",
        "access_level": 40,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Agri
            AgriPermission.WORKER_DASHBOARD_VIEW,
        ],
    },


    # 💰 Finance
    {
        "code": RoleCode.STAFF,
        "name": "Finance",
        "description": "Manage farm financial transactions and cost tracking",
        "access_level": 70,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Agri
            AgriPermission.FINANCE_DASHBOARD_VIEW,
        ],
    },
]