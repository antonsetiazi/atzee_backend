# hrms/api/urls.py

from django.urls import include, path

urlpatterns = [
    path(
        "employees/",
        include("hrms.api.employee.urls"),
    ),
    path(
        "attendance/",
        include("hrms.api.attendance.urls"),
    ),
    path(
        "leave/",
        include("hrms.api.leave.urls"),
    ),
    path(
        "payroll/",
        include("hrms.api.payroll.urls"),
    ),
    path(
        "dashboard/",
        include("hrms.api.dashboard.urls"),
    ),
]
