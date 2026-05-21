# hrms/api/employee/urls.py

from django.urls import path

from .views import (
    EmployeeListApi,
    EmployeeOnboardApi,
)

urlpatterns = [
    path("", EmployeeListApi.as_view(), name="employee-list"),
    path("onboard/", EmployeeOnboardApi.as_view(), name="employee-onboard"),
]
