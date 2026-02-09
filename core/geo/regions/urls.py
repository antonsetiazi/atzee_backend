# core/geo/regions/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.geo.regions.views import RegionViewSet

router = DefaultRouter()
router.register("regions", RegionViewSet, basename="region")

urlpatterns = [
    path("", include(router.urls)),
]
