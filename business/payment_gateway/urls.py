# business/payment_gateway/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.payment_gateway.views import (
    PaymentMethodViewSet,
    PaymentGatewayConfigViewSet,
)
from business.payment_gateway.webhooks.midtrans import midtrans_webhook
from business.payment_gateway.webhooks.xendit import xendit_webhook
from business.payment_gateway.views_payment import create_payment_view

router = DefaultRouter()
router.register(r"methods", PaymentMethodViewSet, basename="payment-method")
router.register(r"configs", PaymentGatewayConfigViewSet, basename="payment-config")

urlpatterns = [
    path("create/", create_payment_view),
    # 🔴 webhook
    path("webhook/midtrans/", midtrans_webhook),
    path("webhook/xendit/", xendit_webhook),

    # 🟢 admin API
    path("", include(router.urls)),
]