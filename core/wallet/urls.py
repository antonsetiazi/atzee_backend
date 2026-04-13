# core/wallet/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.wallet.views import WalletViewSet

router = DefaultRouter()
router.register("wallet", WalletViewSet, basename="wallet")

urlpatterns = [
    path("", include(router.urls)),
]