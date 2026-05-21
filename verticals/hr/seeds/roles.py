# verticals/hr/seeds/roles.py

# from accounting.enum.permissions import AccountingPermission
from business.enum.permissions import BusinessPermission
from core.enum.permissions import CorePermission
from core.roles.enums import RoleCode
from verticals.hr.enum.permissions import HrPermission

ROLES = [
    {
        "code": RoleCode.GUEST,
        "name": "Guest",
        "description": "Public visitor (not authenticated)",
        "access_level": 0,
        "default_permissions": [
            HrPermission.GUEST_HOME_VIEW,
        ],
    },
    # Admin tenant: manage users, roles, settings
    {
        "code": RoleCode.ADMIN,
        "name": "Admin",
        "description": "Manage users, roles, and tenant settings",
        "access_level": 10,
        "default_permissions": [
            CorePermission.DASHBOARD_VIEW,
            CorePermission.ADMIN_TENANT_BRANDING_VIEW,
            CorePermission.ADMIN_TENANT_BRANDING_UPDATE,
            CorePermission.ADMIN_USERS_VIEW,
            CorePermission.ADMIN_WIDGETS_VIEW,
            CorePermission.ADMIN_WIDGETS_CREATE,
            CorePermission.ADMIN_WIDGETS_EDIT,
            CorePermission.ADMIN_WIDGETS_DELETE,
            CorePermission.ADMIN_BANK_VIEW,
            CorePermission.ADMIN_BANK_CREATE,
            CorePermission.ADMIN_BANK_EDIT,
            CorePermission.ADMIN_POLICY_VIEW,
            CorePermission.ADMIN_POLICY_CREATE,
            CorePermission.ADMIN_POLICY_EDIT,
            CorePermission.ADMIN_POLICY_DELETE,
            BusinessPermission.USERS_VIEW,
            # AccountingPermission.ACCOUNT_LIST_SELECT,
            # AccountingPermission.JOURNAL_CREATE,
            # AccountingPermission.JOURNAL_VIEW,
            # AccountingPermission.ACCOUNT_VIEW,
            # AccountingPermission.ADMIN_ACCOUNT_VIEW,
            # AccountingPermission.ADMIN_ACCOUNT_CREATE,
            # AccountingPermission.ADMIN_ACCOUNT_EDIT,
            # AccountingPermission.ADMIN_ACCOUNT_DETAIL,
            # AccountingPermission.ADMIN_ACCOUNT_DELETE,
            # AccountingPermission.ADMIN_REPORT_VIEW,
            HrPermission.ADMIN_DASHBOARD_VIEW,
        ],
    },
]
