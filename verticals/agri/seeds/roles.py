# verticals/agri/seeds/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.agri.enum.permissions import AgriPermission


ROLES = [

    # 🌾 Owner (Full Farm Control)
    {
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


    # 🌱 Field Supervisor
    {
        "name": "Field Supervisor",
        "description": "Supervise daily farming activities and workers",
        "access_level": 65,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Agri
            AgriPermission.SUPERVISOR_DASHBOARD_VIEW,
        ],
    },


    # 👨‍🌾 Worker
    {
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