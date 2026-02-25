# core/wallet/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.wallet.views import WalletViewSet

router = DefaultRouter()
router.register("wallets", WalletViewSet, basename="wallet")

wallet_payment = WalletViewSet.as_view({"post": "pay_booking"})

urlpatterns = [
    path("", include(router.urls)),
    path("wallets/pay-booking/<int:booking_id>/", wallet_payment, name="wallet-pay-booking"),
]