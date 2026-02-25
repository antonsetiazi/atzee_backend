# core/payment/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.payment.views import PaymentViewSet

router = DefaultRouter()
router.register("payments", PaymentViewSet, basename="payment")

urlpatterns = [
    path("", include(router.urls)),
]