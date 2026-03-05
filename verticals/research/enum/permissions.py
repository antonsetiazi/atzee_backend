# verticals/research/enum/permissions.py

from enum import Enum

class ResearchPermission(str, Enum):

    DIRECTOR_DASHBOARD_VIEW = "research.director.dashboard.view"
    COMMITTEE_DASHBOARD_VIEW = "research.committee.dashboard.view"
    REVIEWER_DASHBOARD_VIEW = "research.reviewer.dashboard.view"
    PI_DASHBOARD_VIEW = "research.pi.dashboard.view"
    RESEARCHER_DASHBOARD_VIEW = "research.researcher.dashboard.view"
    ASSISTANT_DASHBOARD_VIEW = "research.assistant.dashboard.view"
    FINANCE_DASHBOARD_VIEW = "research.finance.dashboard.view"
    ADMIN_DASHBOARD_VIEW = "research.admin.dashboard.view"

    def __str__(self):
        return self.value