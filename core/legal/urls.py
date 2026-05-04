# core/legal/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.legal.views import PolicyViewSet
from .views_public import get_latest_policy

router = DefaultRouter()
router.register("policies", PolicyViewSet, basename="policy")

urlpatterns = [
    path("", include(router.urls)),
    path("public/policies/latest/", get_latest_policy),
]