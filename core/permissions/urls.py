from django.urls import path
from core.permissions.views import (
    MyPermissionView,
    PermissionCheckView
)

urlpatterns = [
    path("me/", MyPermissionView.as_view()),
    path("check/", PermissionCheckView.as_view()),
]
