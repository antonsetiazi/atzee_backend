# core/account/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.account.views import UpdateProfileView
from core.account.views import UserSettingsView, UserAddressViewSet
from core.account.views import UserBankViewSet

router = DefaultRouter()
router.register(r"address", UserAddressViewSet, basename="user-address")
router.register(r"banks", UserBankViewSet, basename="user-banks")

urlpatterns = [
    path("", include(router.urls)),
    path("profile/", UpdateProfileView.as_view(), name="update-profile"),
    path("settings/", UserSettingsView.as_view(), name="user-settings"),
]
