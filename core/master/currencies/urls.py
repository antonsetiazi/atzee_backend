# core/master/currencies/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.master.currencies.views import CurrencyViewSet


router = DefaultRouter()
router.register(r"currencies", CurrencyViewSet, basename="currency")

urlpatterns = [
    path("", include(router.urls)),
]
