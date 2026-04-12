# core/geo/districts/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.geo.districts.views import DistrictViewSet

router = DefaultRouter()
router.register("districts", DistrictViewSet, basename="district")

urlpatterns = [
    path("", include(router.urls)),
]