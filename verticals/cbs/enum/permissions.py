# verticals/cbs/enum/permissions.py

from enum import Enum

class CbsPermission(str, Enum):

    DIRECTOR_DASHBOARD_VIEW = "cbs.director.dashboard.view"
    BRANCH_MANAGER_DASHBOARD_VIEW = "cbs.branch.manager.dashboard.view"
    CREDIT_OFFICER_DASHBOARD_VIEW = "cbs.credit.officer.dashboard.view"
    TELLER_DASHBOARD_VIEW = "cbs.teller.dashboard.view"
    BACK_OFFICE_DASHBOARD_VIEW = "cbs.back.office.dashboard.view"
    COMPLIANCE_DASHBOARD_VIEW = "cbs.compliance.dashboard.view"
    AUDITOR_DASHBOARD_VIEW = "cbs.auditor.dashboard.view"



    def __str__(self):
        return self.value