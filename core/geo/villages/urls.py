# core/geo/villages/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.geo.villages.views import VillageViewSet

router = DefaultRouter()
router.register("villages", VillageViewSet, basename="village")

urlpatterns = [
    path("", include(router.urls)),
]