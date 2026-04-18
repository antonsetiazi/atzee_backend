# core/master/banks/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.master.banks.views import BankViewSet

router = DefaultRouter()
router.register("banks", BankViewSet, basename="bank")

urlpatterns = [
    path("", include(router.urls)),
]