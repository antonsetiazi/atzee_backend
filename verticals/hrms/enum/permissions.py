# verticals/hrms/enum/permissions.py

from enum import Enum

class HrmsPermission(str, Enum):

    ADMIN_DASHBOARD_VIEW = "hrms.admin.dashboard.view"
    OFFICER_DASHBOARD_VIEW = "hrms.officer.dashboard.view"
    LINE_MANAGER_DASHBOARD_VIEW = "hrms.line.manager.dashboard.view"
    EMPLOYEE_DASHBOARD_VIEW = "hrms.employee.dashboard.view"
    FINANCE_DASHBOARD_VIEW = "hrms.finance.dashboard.view"
    EXECUTIVE_DASHBOARD_VIEW = "hrms.executive.dashboard.view"


    ORGANIZATION_VIEW = "hrms.organization.view"
    ORGANIZATION_MANAGE = "hrms.organization.manage"

    EMPLOYEE_VIEW = "hrms.employee.view"
    EMPLOYEE_MANAGE = "hrms.employee.manage"
    EMPLOYEE_CREATE = "hrms.employee.create"
    EMPLOYEE_UPDATE = "hrms.employee.update"
    EMPLOYEE_DELETE = "hrms.employee.delete"
    EMPLOYEE_APPROVE = "hrms.employee.approve"
    EMPLOYEE_GENERATE = "hrms.employee.generate"

    ATTENDANCE_VIEW = "hrms.attendance.view"
    ATTENDANCE_CREATE = "hrms.attendance.create" 
    ATTENDANCE_UPDATE = "hrms.attendance.update"
    ATTENDANCE_DELETE = "hrms.attendance.delete"
    ATTENDANCE_MANAGE = "hrms.attendance.manage"
    ATTENDANCE_APPROVE = "hrms.attendance.approve"
    ATTENDANCE_GENERATE = "hrms.attendance.generate"

    LEAVE_VIEW = "hrms.leave.view"
    LEAVE_CREATE = "hrms.leave.create" 
    LEAVE_UPDATE = "hrms.leave.update"
    LEAVE_DELETE = "hrms.leave.delete"
    LEAVE_MANAGE = "hrms.leave.manage"
    LEAVE_APPROVE = "hrms.leave.approve"
    LEAVE_GENERATE = "hrms.leave.generate"

    PAYROLL_VIEW = "hrms.payroll.view"
    PAYROLL_CREATE = "hrms.payroll.create" 
    PAYROLL_UPDATE = "hrms.payroll.update"
    PAYROLL_DELETE = "hrms.payroll.delete"
    PAYROLL_MANAGE = "hrms.payroll.manage"
    PAYROLL_APPROVE = "hrms.payroll.approve"
    PAYROLL_GENERATE = "hrms.payroll.generate"
    PAYROLL_JOURNAL_POST = "hrms.payroll.journal.post"

    PERFORMANCE_VIEW = "hrms.performance.view"
    PERFORMANCE_CREATE = "hrms.performance.create" 
    PERFORMANCE_UPDATE = "hrms.performance.update"
    PERFORMANCE_DELETE = "hrms.performance.delete"
    PERFORMANCE_MANAGE = "hrms.performance.manage"
    PERFORMANCE_APPROVE = "hrms.performance.approve"
    PERFORMANCE_GENERATE = "hrms.performance.generate"

    REPORT_VIEW = "hrms.report.view"
    REPORT_CREATE = "hrms.report.create" 
    REPORT_UPDATE = "hrms.report.update"
    REPORT_DELETE = "hrms.report.delete"
    REPORT_MANAGE = "hrms.report.manage"
    REPORT_APPROVE = "hrms.report.approve"
    REPORT_GENERATE = "hrms.report.generate"

    TEAM_DASHBOARD_VIEW = "hrms.team.dashboard.view"
    TEAM_MEMBER_VIEW = "hrms.team.member.view"

    MY_PROFILE_VIEW = "hrms.my.profile.view"
    MY_ATTENDANCE_VIEW = "hrms.my.attendance.view"
    MY_LEAVE_REQUEST = "hrms.my.leave.request"
    MY_PAYROLL_VIEW = "hrms.my.payroll.view"
    MY_PERFORMANCE_VIEW = "hrms.my.performance.view"


    def __str__(self):
        return self.value