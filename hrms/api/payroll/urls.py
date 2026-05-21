# hrms/api/payroll/urls.py

from django.urls import path

from .views import (
    ApprovePayrollApi,
    GeneratePayrollApi,
    PayrollListApi,
)

urlpatterns = [
    path(
        "",
        PayrollListApi.as_view(),
        name="payroll-list",
    ),
    path(
        "generate/",
        GeneratePayrollApi.as_view(),
        name="payroll-generate",
    ),
    path(
        "<uuid:pk>/approve/",
        ApprovePayrollApi.as_view(),
        name="payroll-approve",
    ),
]
