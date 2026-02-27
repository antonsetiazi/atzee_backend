# core/account/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.account.views import UserSettingsView, UserAddressViewSet

router = DefaultRouter()
router.register(r"address", UserAddressViewSet, basename="user-address")

urlpatterns = [
    path("", include(router.urls)),
    path("settings/", UserSettingsView.as_view(), name="user-settings"),
]
