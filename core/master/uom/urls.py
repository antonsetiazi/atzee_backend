# core/master/uom/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.master.uom.views import UOMViewSet


router = DefaultRouter()
router.register(r"uoms", UOMViewSet, basename="uom")

urlpatterns = [
    path("", include(router.urls)),
]
