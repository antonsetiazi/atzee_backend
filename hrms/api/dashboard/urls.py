# hrms/api/dashboard/urls.py

from django.urls import path

from .views import HRMSDashboardApi

urlpatterns = [
    path(
        "",
        HRMSDashboardApi.as_view(),
        name="hrms-dashboard",
    ),
]
