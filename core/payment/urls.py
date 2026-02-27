# core/payment/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.payment.views import PaymentViewSet
from core.payment.webhooks import midtrans_webhook 
from core.payment.webhooks import xendit_webhook 


router = DefaultRouter()
router.register("payments", PaymentViewSet, basename="payment")

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += [
    path(
        "webhooks/midtrans/",
        midtrans_webhook,
        name="midtrans-webhook"
    ),
]

urlpatterns += [
    path(
        "webhooks/xendit/",
        xendit_webhook,
        name="xendit-webhook"
    ),
]