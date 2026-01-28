from django.urls import path
from core.tenants.views import (
    TenantListView,
    TenantSwitchView,
    CurrentTenantView,
)

urlpatterns = [
    path("", TenantListView.as_view(), name="tenant-list"),
    path("current/", CurrentTenantView.as_view(), name="tenant-current"),
    path("switch/", TenantSwitchView.as_view(), name="tenant-switch"),
]
