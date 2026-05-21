# hrms/api/leave/urls.py

from django.urls import path

from .views import (
    ApplyLeaveApi,
    ApproveLeaveApi,
    PendingLeaveApi,
)

urlpatterns = [
    path("", PendingLeaveApi.as_view(), name="leave-list"),
    path("apply/", ApplyLeaveApi.as_view(), name="leave-apply"),
    path(
        "<uuid:pk>/approve/", ApproveLeaveApi.as_view(), name="leave-approve"
    ),
]
