# core/geo/spatial/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.geo.spatial.views import GeoLocationViewSet


router = DefaultRouter()
router.register(r"spatial/locations", GeoLocationViewSet, basename="spatial-location")

urlpatterns = [
    path("", include(router.urls)),
]
